import random
from check import checkcard

def bcbanker () :
    sumscore = 0

    print ("***** BANKER *****")
    
    bankercard1 = random.randint(1,13)
    card = bankercard1
    checkcard(card)
    if bankercard1 >= 10 :
        bankercard1 = 0

    bankercard2 = random.randint(1,13)
    card = bankercard2
    checkcard(card)
    if bankercard2 >= 10 :
        bankercard2 = 0
    
    sumscore = (bankercard1 + bankercard2)%10

    if sumscore == 8 :
        print("*** POK 8!!! ****")
        return sumscore
    elif sumscore == 9 :
        print("*** POK 9!!! ****")
        return sumscore


    if sumscore <= 5 :
        bankercard3 = random.randint(1,13)
        card = bankercard3
        checkcard(card)
        if bankercard3 >= 10 :
            bankercard3 = 0
        sumscore = (sumscore + bankercard3)%10
        return sumscore
    elif sumscore > 5 and sumscore < 8 :
        return sumscore
    else :
        return sumscore