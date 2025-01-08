import random
from TD import TigerDragon
from BC import Baccarat
from BJPlay import BJPlayer
from signin import*

status_user()

money = 1000

def menu(money) :
    status1 = "Y"
    status2 = "Y"
    status3 = "Y"
    while money > 0 :
        print (f"Your Balance : {money}")
        print("******SELECT GAME******")
        print("1. TigerDragon")
        print("2. Baccarat")
        print("3. BlackJack")
        print("0. Exit")

        while True :
            try :
                select = int(input("SelectGame : "))
                if select != 0 and select != 1 and select != 2 and select !=3 :
                    print ("Plese select number 1-3")
                else :
                    break
            except :
                print("Plese select number 1-3")
                
        if select == 1 :
            while money > 0 :
                money = TigerDragon(money)
                print("Your Balance :",money)
                if money > 0 :
                    while True :
                        try :
                            status1 = str(input("CONTINUE (Y/N): "))
                            status1 = status1.upper()
                            if status1 != "Y" and "N" :
                                print ("Please Select Y/N")
                            if status1 == "N" :
                                break
                            if status1 == "Y" :
                                break
                        except :
                            print ("Please Select Y/N")
                if status1 == "N" :
                    break

        elif select == 2 :
            while money > 0 :
                money = Baccarat(money)
                print("Your Balance :",money)
                if money > 0 :
                     while True :
                        try :
                            status2 = str(input("CONTINUE (Y/N): "))
                            status2 = status2.upper()
                            if status2 != "Y" and "N" :
                                print ("Please Select Y/N")
                            if status2 == "N" :
                                break
                            if status2 == "Y" :
                                break
                        except :
                            print ("Please Select Y/N")
                if status2 == "N" :
                    break
                
        elif select == 3 :
            while money > 0 :
                money = BJPlayer(money)
                print("Your Balance :",money)
                if money > 0 :
                     while True :
                        try :
                            status3 = str(input("CONTINUE (Y/N): "))
                            status3 = status3.upper()
                            if status3 != "Y" and "N" :
                                print ("Please Select Y/N")
                            if status3 == "N" :
                                break
                            if status3 == "Y" :
                                break
                        except :
                            print ("Please Select Y/N")
                if status3 == "N" :
                    break
        elif select == 0 :
            print ("Thank you for play our games")
            break
    if money <= 0 :
        print ("***Sorry but you don't have money to play***") 
            
                
menu(money)