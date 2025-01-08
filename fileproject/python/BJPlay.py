from BJ import Blackjack
from BJ2 import Blackjack2

def BJPlayer(money) : 
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

    print("***PROGRAM CARD***")
    programscore = Blackjack2()
    if programscore == 21 :
        print ("*** BLACK JACK!!! ***")

    print("***YOUR CARD***")
    scoreplayer = Blackjack()
    if scoreplayer == 21 :
        print ("*** BLACK JACK!!! ***")
    print("-"*30)

    if programscore > 21 :
        programscore = 0
    if scoreplayer > 21 :
        scoreplayer = 0
    

    if programscore > scoreplayer :
        print ("*** YOU LOSE ***")
        print (f"- {bet}")
    elif programscore < scoreplayer :
        print ("*** YOU WIN ****")
        print (f"+ {bet}")
        money = money + (bet*2)
    elif programscore == scoreplayer :
        print ("*** TIE ****")
        money = money + (bet)
    return money



    
