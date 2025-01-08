import random
from check import checkcard

def TigerDragon(money,) : 
    print("-"*30)

    while True :
        try :
            bet = int(input("Enter your bet : "))
            break
        except :
            print ("Please enter amount")

    if bet > money :
        bet = money

    money = money-bet

    while True :
        while True :
            while True :
                try :
                    TD = str(input("Tiger / DRAGON / Tie : "))
                    TD = TD.upper()
                    print (TD)
                    if TD != "Tiger" or "DRAGON" or "TIE" :
                        print ("Please select Tiger / DRAGON / Tie")
                    if TD == "TIGER" :
                        break
                    if TD == "DRAGON" :
                        break
                    if TD == "TIE" :
                        break
                except :
                    print ("Please select Tiger / DRAGON / Tie")

            TD = TD.upper()

            print("****TIGER****")
            numbertiger = random.randint(1,13)
            card = numbertiger
            checkcard(card)
            print("***TIGER SCORE :",card,"***")
            
            print("****DRAGON****")
            numberdragon = random.randint(1,13)
            card = numberdragon
            checkcard(card)
            print("***DRAGON SCORE :",card,"***")
            
            print("-"*30)

            if numberdragon == numbertiger and TD == "TIE":
                money = money+(bet*8)
                print("**YOU WIN**")
                print("+",bet*7)
            elif numberdragon > numbertiger and TD == "DRAGON":
                money = money+(bet*2)
                print("**YOU WIN**")
                print("+",bet*1)
            elif numberdragon < numbertiger and TD == "TIGER":
                money = money+(bet*2)
                print("**YOU WIN**")
                print("+",bet*1)
            else :
                print("**YOU LOSE**")
                print("-",bet)
            return money

