import random
from check import checkcard

def bcplayer () :
    sumscore = 0

    print ("***** player *****")
    
    playercard1 = random.randint(1,13)
    card = playercard1
    checkcard(card)
    if playercard1 >= 10 :
        playercard1 = 0

    playercard2 = random.randint(1,13)
    card = playercard2
    checkcard(card)
    if playercard2 >= 10 :
        playercard2 = 0
    
    sumscore = (playercard1 + playercard2)%10

    if sumscore == 8 :
        print("*** POK 8!!! ****")
        return sumscore
    elif sumscore == 9 :
        print("*** POK 9!!! ****")
        return sumscore


    if sumscore <= 5 :
        playercard3 = random.randint(1,13)
        card = playercard3
        checkcard(card)
        if playercard3 >= 10 :
            playercard3 = 0
        sumscore = (sumscore + playercard3)%10
        return sumscore
    elif sumscore > 5 and sumscore < 8 :
        return sumscore
    else :
        return sumscore