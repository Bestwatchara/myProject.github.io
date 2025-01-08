import random

from bcplayer import bcplayer
from bcbanker import bcbanker

def Baccarat(money) : 
    print("-"*30)

    while True :
        try :
            bet = int(input("Enter your bet : "))
            break
        except :
            print ("Please enter amount")

    if bet > money :
        bet = money
    money = money - bet

    while True :
        while True :
            try :
                BC  = str(input("Player / Banker / Tie : "))
                BC = BC.upper()
                print (BC)
                if BC != "PLAYER" or "BANKER" or "TIE" :
                    print ("Please select Player / Banker / Tie")
                if BC == "PLAYER" :
                    break
                if BC == "BANKER" :
                    break
                if BC == "TIE" :
                    break
            except :
                print ("Please select Player / Banker / Tie")

        sumplayer = bcplayer()

        print(f"PLAYER SCORE {sumplayer}\n**********")

        sumbanker = bcbanker()
        print(f"BANKER SCORE {sumbanker}\n**********")
        
        if sumplayer > sumbanker : 
            print("**PLAYER WIN**")
        elif sumplayer < sumbanker :
            print("**BANKER WIN**")
        elif sumplayer == sumbanker :
            print("**TIE**")

        print("-"*30)

        if sumplayer == sumbanker and BC == "TIE" :
            money = money + (bet*8)
            print("**YOU WIN**")
            print("+",bet*7)
        elif sumplayer > sumbanker and BC == "PLAYER" :
            money = money + (bet*2)
            print("**YOU WIN**")
            print("+",bet*1)
        elif sumplayer < sumbanker and BC == "BANKER" : 
            money = money + (bet*1.95)
            print("**YOU WIN**")
            print("+",bet*0.95)
        elif sumplayer == sumbanker and BC != "TIE" :
            print("TAKE BACK",bet)
            money = money + bet
        else :
            print("**YOU LOSE**")
            print("-",bet)

        return money

