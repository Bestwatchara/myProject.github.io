import random
from tabnanny import check
from check import checkcard

def Blackjack2() :
    sumscore = 0
    
    score1 = random.randint(1,13)
    card = score1
    checkcard(card)
    if score1 >= 10 :
        score1 = 10

    score2 = random.randint(1,13)
    card = score2
    checkcard(card)
    if score2 >= 10 :
        score2 = 10
    
    sumscore = score1 + score2
    
    if score1 == 1 and score2 == 10 :
        sumscore = 21
    elif score2 == 1 and score1 == 10 :
        sumscore = 21

    if sumscore == 21 :
        print("PROGRAM SCORE :",sumscore)
        return sumscore     
        
    while True :
        score3 = random.randint(1,13)
        card = score3
        checkcard(card)
        if score3 >= 10 :
            score3 = 10
        sumscore = sumscore + score3
        if sumscore >= 17 :
            print("PROGRAM SCORE :",sumscore)
            return sumscore
        if sumscore > 21 :
            print("PROGRAM SCORE :",sumscore)
            return sumscore


    

    