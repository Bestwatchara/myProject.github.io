import gradio as gr
import requests

API_URL = "http://localhost:8000/ask"

def process_query(query):
    try:
        response = requests.post(
            API_URL,
            json={"question": query, "top_k": 3},
            timeout=30
        )
        
        if response.status_code != 200:
            return f"⚠️ ข้อผิดพลาดจากเซิร์ฟเวอร์: {response.text}"
            
        data = response.json()
        
        # จัดรูปแบบผลลัพธ์
        output = f"""
        ## คำตอบ:  
        {data['answer']}
        
        ### เอกสารอ้างอิง:  
        {chr(10).join([f"- {doc['content'][:200]}..." for doc in data['documents']])}
        """
        return output
    
    except requests.exceptions.RequestException as e:
        return f"🔌 ข้อผิดพลาดการเชื่อมต่อ: {str(e)}"
    except Exception as e:
        return f"❌ ข้อผิดพลาดทั่วไป: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🧠 TISCO AI Advisor")
    
    with gr.Row():
        input_box = gr.Textbox(
            label="คำถามของคุณ", 
            placeholder="ถามเกี่ยวกับการลงทุน...",
            max_lines=3
        )
        output_box = gr.Markdown()
    
    submit_btn = gr.Button("ส่งคำถาม", variant="primary")
    submit_btn.click(fn=process_query, inputs=input_box, outputs=output_box)

if __name__ == "__main__":
    demo.launch(
        server_port=7860,
        share=True,
        show_error=True
    )