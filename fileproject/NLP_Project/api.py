import os
import time
import torch
import faiss
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.docstore.document import Document
from contextlib import asynccontextmanager
import transformers
import os
from fastapi.middleware.cors import CORSMiddleware
from datasets import load_dataset
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

class DocumentResponse(BaseModel):
    content: str
    metadata: dict

class APIResponse(BaseModel):
    question: str
    answer: str
    documents: list[DocumentResponse]
    processing_time: float

FAISS_INDEX_PATH = "C:/Users/nottc/Downloads/faiss_index.faiss"
EMBEDDINGS_PATH = "C:/Users/nottc/Downloads/document_embeddings.npy"

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Downloading...")

    ds = load_dataset("airesearch/WangchanThaiInstruct")
    train_data = ds["train"]
    documents = [
        {"text": example["Instruction"], "answer": example["Output"]}
        for example in train_data
    ]
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50
    )

    app.state.document_objects = []
    for doc in documents:
        texts = text_splitter.split_text(doc["text"])
        for text in texts:
            app.state.document_objects.append(
                Document(
                    page_content=text,
                    metadata={"answer": doc["answer"]}
                )
            )
    print("Downloading Data Success")
    app.state.embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-mpnet-base-v2',device="cuda")
    print("Downloading Embedder Success")
    app.state.tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B")
    print("Downloading Tokenizer Success")
    app.state.model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B",torch_dtype=torch.float16,device_map="auto")
    print("Downloading Model Success")

    app.state.pipe = pipeline(
    "text-generation",
    model=app.state.model,
    tokenizer=app.state.tokenizer,
    temperature=0.65,
    top_k=40,
    top_p=0.8,  # ลดการสุ่ม
    repetition_penalty=1.5,  # เพิ่มค่าลดซ้ำซ้อน
    truncation=True,
    pad_token_id=app.state.tokenizer.eos_token_id,
    eos_token_id=app.state.tokenizer.eos_token_id,
    do_sample=True,
    )

    app.state.llm = HuggingFacePipeline(pipeline=app.state.pipe)
    
    # 4. โหลดเอกสารและ FAISS Index
    app.state.document_embeddings = np.load(EMBEDDINGS_PATH)

    # โหลด FAISS Index
    app.state.index = faiss.read_index(str(FAISS_INDEX_PATH))

    print("Download suceess")

    yield

    print("🔴 ปิดทรัพยากร...")


app = FastAPI(
    title="Thai Financial AI Advisor",
    description="API สำหรับให้คำแนะนำการลงทุนด้วย RAG และโมเดล Llama",
    lifespan=lifespan
)

# โหลดข้อมูลเมื่อเริ่มแอป


@app.get("/")
def health_check():
    return {"status": "ready", "model": "Llama-3.2-1B"}

@app.post("/ask", response_model=APIResponse)
async def ask_question(request: QueryRequest):
    try :
        start_time = time.time()
        # ค้นหาข้อมูล
        query_embedding = app.state.embedder.encode([request.question], normalize_embeddings=True)
        distances,indices = app.state.index.search(query_embedding, request.top_k)
        retrieved_docs = [app.state.document_objects[i] for i in indices[0]]
        
        # สร้างบริบท
        context = "\n".join([doc.metadata["answer"] for doc in retrieved_docs])
        
        # สร้างคำตอบ
        prompt = f"""<|system|>
        คุณเป็นผู้ช่วย AI ที่มีความเชี่ยวชาญด้านการเงิน
        ใช้ข้อมูลต่อไปนี้ตอบคำถามอย่างถูกต้องและสมบูรณ์:
        {context}
        </s>
        <|user|>
        {request.question}
        </s>
        <|assistant|>"""
        
        response = app.state.llm.invoke(prompt)
        answer = response.split("</s>")[0].strip()
        
        processing_time = time.time() - start_time

        return APIResponse(
            question=request.question,
            answer=answer,
            documents=[
                DocumentResponse(
                    content=doc.page_content,
                    metadata=doc.metadata
                ) for doc in retrieved_docs
            ],processing_time=round(processing_time, 4)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)