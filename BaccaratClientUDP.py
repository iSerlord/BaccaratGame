from socket import *
import random
import time
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
# message = input('Input lowercase sentence: ')
def registerGame() :
    while True:
        registerUsername = input("username : ") 
        password = input("password : ")
        concat = registerUsername + " " + password + " " +"register"
        #print (concat)
        clientSocket.sendto(concat.encode(),(serverName, serverPort))
        checkUsername, serverAddress = clientSocket.recvfrom(2048)
        checkUsername = checkUsername.decode()
        if (checkUsername == "True") :
            print ("Register Success")
            break
        else :
            print ("Register failed, This " + registerUsername + " already taken" )
def loginGame() :
    while True:
        loginUsername = input("username : ") 
        loginPassword = input("password : ")
        concat = loginUsername + " " + loginPassword + " " + "login"
        clientSocket.sendto(concat.encode() ,(serverName, serverPort))
        checkUsername, serverAddress = clientSocket.recvfrom(2048)
        checkUsername = checkUsername.decode()
        if (checkUsername == "True") :
            print ("Login Success")
            break 
        elif (checkUsername == "False already") :
            print ("Login Failed. another has login this id")
        else :
            print ("Login Failed. Wrong username or password")

def deposit(iduser,money):
    depo = iduser + " " + str(money) + " " + "deposit"
    clientSocket.sendto(depo.encode() ,(serverName, serverPort))

def withdraw(iduser,money):
    withmoney = iduser + " " + str(money) + " " + "withdraw"
    clientSocket.sendto(withmoney.encode() ,(serverName, serverPort))    

def logOutGame(user , idUser) :
    logout = user + " " + idUser +" "+"logout"
    clientSocket.sendto(logout.encode() ,(serverName, serverPort))            

def playgame(money ,idp , user) :
    selfMoney = money
    
    while True :
        play =  user + " " + str(idp) + " " +"playgame"
        clientSocket.sendto(play.encode() ,(serverName, serverPort))
        print ("you have amount = " + str(selfMoney))
        while True :
            inputMoney = (input("How much you bet ? : "))
            
            if (inputMoney.isnumeric() and int(inputMoney) > 0):
                inputMoney = int(inputMoney)
                if ((selfMoney) < inputMoney) :
                    print ("cant bet")
                    continue
                break
            else :
                print ("Error")
        
        
        while True :
            inputBet = input("[B]anker , [P]layer , [D]raw : ")
            
            if (inputBet == 'B' or inputBet == 'b' or inputBet == 'P' or inputBet == 'p'
            or inputBet == 'D' or inputBet == 'd'):
                inputMoney = int(inputMoney)
                break
            else :
                print ("Error")
        # inputBet = input("[B]anker , [P]layer , [D]raw : ")
        concat = str(inputMoney) + " " + inputBet 
        clientSocket.sendto(concat.encode() ,(serverName, serverPort))
        # concat = inputMoney + " " + inputBet + " " + "play"
        cardPlayer, serverAddress = clientSocket.recvfrom(2048)
        cardBanker, serverAddress = clientSocket.recvfrom(2048)
        cardPlayer = cardPlayer.decode()
        cardBanker = cardBanker.decode()
        cardPlayer = cardPlayer.split(" ")
        cardBanker = cardBanker.split(" ")

        p1 = cardPlayer[0]
        p2 = cardPlayer[1]
        b1 = cardBanker[0]
        b2 = cardBanker[1]
        # card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        # b1 = random.choice(card)
        # b2 = random.choice(card)
        # p1 = random.choice(card)
        # p2 = random.choice(card)
        
        print ("Player Card : " + p1 + " " + p2) , time.sleep(1.5)
        print ("Banker Card : " + b1 + " " + b2) , time.sleep(1.5)

        if (b1 == 'J' or b1 == 'Q' or b1 == 'K') :
            b1 = 0
        if (b1 != 'J' or b1 != 'Q' or b1 != 'K') :
            b1 = int(b1)    
        if (b2 == 'J' or b2 == 'Q' or b2 == 'K') :
            b2 = 0
        if (b2 != 'J' or b2 != 'Q' or b2 != 'K') :
            b2 = int(b2)    
        
        if (p1 == 'J' or p1 == 'Q' or p1 == 'K') :
            p1 = 0
        if (p1 != 'J' or p1 != 'Q' or p1 != 'K') :
            p1 = int(p1)    
        if (p2  == 'J' or p2  == 'Q' or p2  == 'K') :
            p2  = 0
        if (p2 != 'J' or p2 != 'Q' or p2 != 'K') :
            p2 = int(p2)          
        
        if (((p1 + p2 >= 0 and p1 + p2 <=5 ) or (p1 + p2 >= 10 and p1 + p2 <=15 ))
            and ((b1+b2 >=0  and b1+b2 <= 5 ) or (b1+b2 >=10  and b1+b2 <= 15 ))) :
            # p3 = random.choice(card)
            # b3 = random.choice(card)
            cardPlayer1, serverAddress = clientSocket.recvfrom(2048)
            cardBanker1, serverAddress = clientSocket.recvfrom(2048)
            p3 = cardPlayer1.decode()
            b3 = cardBanker1.decode()
            print ("Player Extra Card : " + str(p3)) , time.sleep(1.5)
            print ("Banker Extra Card : " + str(b3)) , time.sleep(1.5)
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5)
            
            # if (p3 == 'J' or p3 == 'Q' or p3 == 'K') :
            #     p3 = 0
            # if (p3 != 'J' or p3 != 'Q' or p3 != 'K') :
            #     p3 = int(p3)
            # if (b3 == 'J' or b3 == 'Q' or b3 == 'K') :
            #     b3 = 0
            # if (b2 != 'J' or b3 != 'Q' or b3 != 'K') :
            #     b3 = int(b3)    
                
            # if (b3 == 'J' or b3 == 'Q' or b3 == 'K') :
            #     b3 = 0 
            
            # p = p1 + p2 + p3
            # b = b1 + b2 + b3

            # if (p >= 10 and p < 20) :
            #     p = p - 10
            # if (p >= 20) :
            #     p = p - 20
            # if (b >= 10 and b < 20) :
            #     b = b - 10
            # if (b >= 20) :
            #     b = b - 20          
            # if (p > b) :
            #     print ("Player win") , time.sleep(1.5)
            #     if (inputBet == 'p' or inputBet == 'P') :
            #         print ("You earn money " + str(inputMoney) )
            #         selfMoney = selfMoney + inputMoney
            #     else :
            #         print ("You loss money " + str(inputMoney) )
            #         selfMoney = selfMoney - inputMoney    
            # elif (p == b) :     
            #     print ("Draw") , time.sleep(1.5)
            #     if (inputBet == 'D' or inputBet == 'd') :
            #         print ("You earn money " + str(inputMoney) )
            #         selfMoney = selfMoney + inputMoney
            #     else :
            #         print ("You loss money " + str(inputMoney) )
            #         selfMoney = selfMoney - inputMoney
            # elif (p < b) :
            #     print ("Banker win") , time.sleep(1.5)
            #     if (inputBet == 'B' or inputBet == 'b') :
            #         print ("You earn money " + str(inputMoney) )
            #         selfMoney = selfMoney + inputMoney
            #     else :
            #         print ("You loss money " + str(inputMoney) )
            #         selfMoney = selfMoney - inputMoney   
        
        elif (((p1 + p2 >= 0 and p1 + p2 <=5 ) or (p1 + p2 >= 10 and p1 + p2 <=15 ))
            and ((b1+b2 >=6  and b1+b2 <= 7 ) or (b1+b2 >=16  and b1+b2 <= 17 ))) :
            cardPlayer1, serverAddress = clientSocket.recvfrom(2048)
            p3 = cardPlayer1.decode()
            print ("Player Extra Card : " + str(p3)) , time.sleep(1.5)
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5)             
        
        elif (((p1 + p2 >= 0 and p1 + p2 <=7) or (p1 + p2 >= 10 and p1 + p2 <=17 ))
            and (b1 + b2 == 8 or b1 + b2 == 9 or b1 + b2 == 18 or b1 + b2 == 19)) :
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5)
        
        elif (( p1 + p2 == 6 or p1 + p2 == 7 or p1 + p2 == 16 or p1 + p2 == 17)
            and ((b1+b2 >=0  and b1+b2 <= 5 ) or (b1+b2 >=10  and b1+b2 <= 15 ))) :     
            cardPlayer1, serverAddress = clientSocket.recvfrom(2048)
            b3 = cardPlayer1.decode()
            print ("Banker Extra Card : " + str(b3)) , time.sleep(1.5)
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5) 

        elif (( p1 + p2 == 6 or p1 + p2 == 7 or p1 + p2 == 16 or p1 + p2 == 17 ) 
        and (b1 + b2 == 6 or b1 + b2 == 7 or b1 + b2 == 16 or b1 + b2 == 17)) :     
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5) 

        elif (( p1 + p2 == 8 or p1 + p2 == 9 or p1 + p2 == 18 or p1 + p2 == 19 ) 
        and ((b1+b2 >=0  and b1+b2 <= 7 ) or (b1+b2 >=10  and b1+b2 <= 17 ))) :     
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5) 

        elif (( p1 + p2 == 8 or p1 + p2 == 9 or p1 + p2 == 18 or p1 + p2 == 19 ) 
        and (b1 + b2 == 8 or b1 + b2 == 9 or b1 + b2 == 18 or b1 + b2 == 19 )) :
            notice, serverAddress = clientSocket.recvfrom(2048)
            print(notice.decode()) , time.sleep(1.5)
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode()) , time.sleep(1.5) 

        myMoney, serverAddress = clientSocket.recvfrom(2048)
        selfMoney = int(myMoney.decode())
        if (selfMoney == 0) :
            print ("You not have money")
            return selfMoney 

        
        c1 = 0
        while True : 
            order = input("[P]lay or [Q]uit : ")
            if (order == 'P' or order == 'p') :
                c1 = 1
                break
            elif (order == 'Q' or order == 'q') :
                c1 = 2
                return selfMoney 
            else :
                print ("Error")
            
        if (c1 == 1) :
            continue
        else :
            break

    # clientSocket.sendto(concat.encode(),(serverName, serverPort))                
while True :
    while True:
        print ("---------- Welcome to baccarat Game ----------")
        command = input("[L]ogin or [R]egister : ")
        if (command == 'R' or command == 'r') :
            registerGame()
        elif (command == 'L' or command == 'l') :
            loginGame()
            break
        else :
            print("Error please try again")       
    # print ("success")

    # while True:
        # print ("---------- Welcome to Barcara Game ----------")
    username , serverAddress = clientSocket.recvfrom(2048)
    idplayer , serverAddress = clientSocket.recvfrom(2048)
    money , serverAddress = clientSocket.recvfrom(2048)
    username = username.decode()
    idplayer = idplayer.decode()
    print (idplayer)
    money = int(money.decode())
    print ("Hi " + username  )
    # print (username)
    # print (idplayer)
    # print (money)

    while True :
        print ("Money = " + str(money))
        command = input("[P]lay game, [D]eposit, [W]ithdraw , [L]ogout: ")
        if (command == 'P' or command == 'p') :
            if (int(money) <= 0) :
                print ("Please deposit money in account")
            else :
                money = playgame(money ,int(idplayer),username)
        elif (command == 'D' or command == 'd') :
            print ("you have amount = " + str(money))
            depoMoney = (input("how much you want to deposit : ")) 
            try : 
                depoMoney = int(depoMoney)
                if (depoMoney <= 0) :
                    print ("Error")
                else :
                    print (idplayer)
                    deposit(idplayer,depoMoney)
                    money = money + depoMoney
                    
                    print ("----Deposit Complete----")
                    # print ("You have money : " + str(money))
            except :
                print ("Not number")
            
            
        elif (command == 'W' or command == 'w') :
            print ("you have amount = " + str(money))
            WithMoney = (input("how much you want to withdraw : ")) 
            try : 
                WithMoney = int(WithMoney)
                if (WithMoney <= 0) :
                    print ("Error")
                else :
                    if (WithMoney > money) :
                        print ("Error")
                    else :
                        withdraw(idplayer,WithMoney)
                        money = money - WithMoney
                        print ("----Withdraw Complete----")
                        # print ("You have money : " + str(money))     
            except :
                print ("Not number")
            
        elif (command == 'L' or command == 'l') :
            check = 0
            while True :
                checkout = input("Are you sure Logout ? [Y/N] : ")
                if (checkout == 'Y' or checkout == 'y') :
                    check = check + 1
                    logOutGame(username,idplayer)
                    break
                elif (checkout == 'N' or checkout == 'n') :
                    break
                else :
                    print ("Error please try again")
            if (check == 1) :
                break    
        else :
            print("Error please try again")     
        

#clientSocket.sendto(message.encode(), (serverName, serverPort))
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print(modifiedMessage.decode())
clientSocket.close()