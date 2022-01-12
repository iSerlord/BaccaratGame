from socket import *
import random
import time
#print (socket.gethostbyname(socket.gethostname()))
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
# num = 0
usernameList = ["admin"]
passwordList = ["1234"]
playerIDList = [1]
IDstart = 1
statusList = ["online"]
money = [0]
print("The server is ready to receive")



def checkJQK(c3) :
    if (c3 == 'J' or c3 == 'Q' or c3 == 'K') :
        c3 = 0
    return c3

def checkJQK2(p3 ,b3) :
    if (p3 == 'J' or p3 == 'Q' or p3 == 'K') :
        p3 = 0
    if (b3 == 'J' or b3 == 'Q' or b3 == 'K') :
        b3 = 0
    return [p3,b3]

def checkpoint(p,b) :
    if (p > b) :
        return "player"                
           
    elif (p == b) :     
        return "draw"
       
    else :
        return "banker"
                            


while True:
    # usernamePlayer
    # passwordPlayer
    receiveConcat, clientAddress = serverSocket.recvfrom(2048)
    receiveConcat = receiveConcat.decode()
    #print (receiveConcat)
    Player = receiveConcat.split(" ")
    Para1 = Player[0]
    para2 = Player[1]
    command = Player[2]
    #print (Player)
    if (command == "register") :
        check = 0 
        for username in usernameList :
            if (username == Para1):
                check = check + 1 
                break
        if (check > 0) :
            checkRegister = "False"
            serverSocket.sendto(checkRegister.encode(), clientAddress)
            print ("< 400 > UsernameAlreadyTaken")
        elif (check == 0) :
            IDstart =  IDstart + 1
            usernameList.append(Para1)
            passwordList.append(para2)
            playerIDList.append(IDstart)
            statusList.append("offline")
            money.append(0)
            checkRegister = "True"
            serverSocket.sendto(checkRegister.encode(), clientAddress)
            print ("< 200 > RegisterComplete")
            # print (usernameList)
            # print (passwordList)
            # print (playerIDList)
            # print (statusList)
            # print (money)

    elif (command == "login") :
        checkPassword = 0
        User = False
        for username in usernameList :
            if (username == Para1):
                if (passwordList[checkPassword] == para2) :
                    User = True
                    break
            checkPassword = checkPassword + 1
        if (User == False) :
            checkLogin = "False"
            serverSocket.sendto(checkLogin.encode(), clientAddress)
            print ("< 401 > LoginFailed")
        else :
            if (statusList[checkPassword] == "offline") :
                statusList[checkPassword] = "online"
                checkLogin = "True"
                serverSocket.sendto(checkLogin.encode(), clientAddress)
                # concatPlayer = usernameList[checkPassword] + " " + playerIDList[checkPassword] + " " 
                # + money[checkPassword]
                # print (concatPlayer )
                iduser = str(playerIDList[checkPassword])
                moneyPlayer = str(money[checkPassword]) 
                serverSocket.sendto(usernameList[checkPassword].encode(), clientAddress)
                serverSocket.sendto(iduser.encode(), clientAddress)
                serverSocket.sendto(moneyPlayer.encode(), clientAddress)
                print ("< 201 > LoginComplete")
            else :
                checkLogin = "False already"
                serverSocket.sendto(checkLogin.encode(), clientAddress)
                print ("< 401 > LoginFailed")
    elif (command == "logout") :
        statusList[int(para2) - 1] = "offline"
        print ("< 206 > LogoutComplete")
    
    
    # Concat, clientAddress = serverSocket.recvfrom(2048)
    # Concat = Concat.decode()
    # Player1 = Concat.split(" ")
    # IDplayer = int(Player1[0])
    # commandPage2 = Player1[1]
    elif (command == "deposit") :
        
        user = int(Para1)
        depoMoney = int(para2)
        money[user - 1] = money[user - 1] + depoMoney
        print ("< 202 > DepositComplete")

    elif (command == "withdraw") :
        
        user = int(Para1)
        withMoney = int(para2)
        money[user - 1] = money[user - 1] - withMoney
        print ("< 203 > WithdrawComplete")    

        
    elif (command == "playgame") :
        IDplayer = int(para2)
        Concat2, clientAddress = serverSocket.recvfrom(2048)
        Concat2 = Concat2.decode()
        # print (Concat2)
        play = Concat2.split(" ")
        moneyTobet = play[0]
        moneyTobet = int(moneyTobet)
        # print (type(moneyTobet))
        bet = play[1]
        print("....Random card....."), time.sleep(1.5)
        card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
        b1 = random.choice(card)
        b2 = random.choice(card)
        p1 = random.choice(card)
        p2 = random.choice(card)
        player = str(p1) + " " + str(p2)
        banker = str(b1) + " " + str(b2)
        serverSocket.sendto(player.encode(), clientAddress)
        serverSocket.sendto(banker.encode(), clientAddress)
        if (b1 == 'J' or b1 == 'Q' or b1 == 'K') :
            b1 = 0
        if (b2 == 'J' or b2 == 'Q' or b2 == 'K') :
            b2 = 0
        if (p1 == 'J' or p1 == 'Q' or p1 == 'K') :
            p1 = 0
        if (p2  == 'J' or p2  == 'Q' or p2  == 'K') :
            p2  = 0

        
        if (((p1 + p2 >= 0 and p1 + p2 <=5 ) or (p1 + p2 >= 10 and p1 + p2 <=15 ))
            and ((b1+b2 >=0  and b1+b2 <= 5 ) or (b1+b2 >=10  and b1+b2 <= 15 ))) :
            p3 = random.choice(card)
            b3 = random.choice(card)
            player3 = str(p3) 
            banker3 = str(b3)
            serverSocket.sendto(player3.encode(), clientAddress)
            serverSocket.sendto(banker3.encode(), clientAddress) 
            
            allsum = checkJQK2(p3,b3)
            p3 = allsum[0]
            b3 = allsum[1]
            
            # if (b1 == 'J' or b1 == 'Q' or b1 == 'K') :
            #     b1 = 0
            # if (b2 == 'J' or b2 == 'Q' or b2 == 'K') :
            #     b2 = 0
            # if (p1 == 'J' or p1 == 'Q' or p1 == 'K') :
            #     p1 = 0
            # if (p2  == 'J' or p2  == 'Q' or p2  == 'K') :
            #     p2  = 0    
            
            # if (p3 == 'J' or p3 == 'Q' or p3 == 'K') :
            #     p3 = 0
                
            # if (b3 == 'J' or b3 == 'Q' or b3 == 'K') :
            #     b3 = 0 
            
            p = p1 + p2 + p3
            b = b1 + b2 + b3

            if (p >= 10 and p < 20) :
                p = p - 10
            if (p >= 20) :
                p = p - 20
            if (b >= 10 and b < 20) :
                b = b - 10
            if (b >= 20) :
                b = b - 20
            
            vsPoint = checkpoint(p,b)
            if (vsPoint == "player") :
                notice = "Player Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'p' or bet == 'P') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5) 
            
            elif (vsPoint == "draw") :
                notice = "Draw"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'D' or bet == 'd') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "banker") :
                notice = "Banker Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'B' or bet == 'b') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)               
            
                                
                
        elif (((p1 + p2 >= 0 and p1 + p2 <=5 ) or (p1 + p2 >= 10 and p1 + p2 <=15 ))
            and ((b1+b2 >=6  and b1+b2 <= 7 ) or (b1+b2 >=16  and b1+b2 <= 17 ))) :
            p3 = random.choice(card)
            player3 = str(p3)
            serverSocket.sendto(player3.encode(), clientAddress)
            allsum = checkJQK(p3)
            p3 = allsum
            
            p = p1 + p2 + p3
            b = b1 + b2 
            if (p >= 10 and p < 20) :
                p = p - 10
            if (p >= 20) :
                p = p - 20
            if (b >= 10 and b < 20) :
                b = b - 10

            vsPoint = checkpoint(p,b)
            if (vsPoint == "player") :
                notice = "Player Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'p' or bet == 'P') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "draw") :
                notice = "Draw"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'D' or bet == 'd') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "banker") :
                notice = "Banker Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'B' or bet == 'b') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)     

        elif (((p1 + p2 >= 0 and p1 + p2 <=7) or (p1 + p2 >= 10 and p1 + p2 <=17 ))
            and (b1 + b2 == 8 or b1 + b2 == 9 or b1 + b2 == 18 or b1 + b2 == 19)) :
            notice = "Banker Win"
            serverSocket.sendto(notice.encode(), clientAddress)
            if (bet == 'B' or bet == 'b') :
                money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                message = "You earn money " + str(moneyTobet)
                serverSocket.sendto(message.encode(), clientAddress)
                serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                print ("< 204 >  UserWin"), time.sleep(1.5)
                print ("< 201 >  PlayComplete"), time.sleep(1.5)  
            else :
                money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                message = "You loss money " + str(moneyTobet)
                serverSocket.sendto(message.encode(), clientAddress)
                serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                print ("< 205 >  UserLose"), time.sleep(1.5)
                print ("< 201 >  PlayComplete"), time.sleep(1.5)
                 
            

        elif (( p1 + p2 == 6 or p1 + p2 == 7 or p1 + p2 == 16 or p1 + p2 == 17)
            and ((b1+b2 >=0  and b1+b2 <= 5 ) or (b1+b2 >=10  and b1+b2 <= 15 ))) :     
            b3 = random.choice(card)
            banker3 = str(b3)
            serverSocket.sendto(banker3.encode(), clientAddress)
            allsum = checkJQK(b3)
            b3 = allsum
            
            p = p1 + p2  
            b = b1 + b2 + b3
            if (p >= 10 and p < 20) :
                p = p - 10
            if (p >= 20) :
                p = p - 20
            if (b >= 10 and b < 20) :
                b = b - 10

            vsPoint = checkpoint(p,b)
            if (vsPoint == "player") :
                notice = "Player Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'p' or bet == 'P') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5) 
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "draw") :
                notice = "Draw"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'D' or bet == 'd') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete") , time.sleep(1.5) 
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "banker") :
                notice = "Banker Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'B' or bet == 'b') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete") , time.sleep(1.5) 
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete") , time.sleep(1.5)

        elif (( p1 + p2 == 6 or p1 + p2 == 7 or p1 + p2 == 16 or p1 + p2 == 17 ) 
        and (b1 + b2 == 6 or b1 + b2 == 7 or b1 + b2 == 16 or b1 + b2 == 17)) :     
            p = p1 + p2 
            b = b1 + b2 
            if (p >= 10 and p < 20) :
                p = p - 10
        
            if (b >= 10 and b < 20) :
                b = b - 10

            vsPoint = checkpoint(p,b)
            if (vsPoint == "player") :
                notice = "Player Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'p' or bet == 'P') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "draw") :
                notice = "Draw"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'D' or bet == 'd') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "banker") :
                notice = "Banker Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'B' or bet == 'b') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
        
        elif (( p1 + p2 == 8 or p1 + p2 == 9 or p1 + p2 == 18 or p1 + p2 == 19 )
        and ((b1+b2 >=0  and b1+b2 <= 7 ) or (b1+b2 >=10  and b1+b2 <= 17 ))) :     
            notice = "Player Win"
            serverSocket.sendto(notice.encode(), clientAddress)
            if (bet == 'p' or bet == 'P') :
                money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                print (money[IDplayer - 1])
                message = "You earn money " + str(moneyTobet)
                serverSocket.sendto(message.encode(), clientAddress)
                serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                print ("< 204 >  UserWin"), time.sleep(1.5)
                print ("< 201 >  PlayComplete") , time.sleep(1.5) 
            else :
                money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet

                message = "You loss money " + str(moneyTobet)
                serverSocket.sendto(message.encode(), clientAddress)
                serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                print ("< 205 >  UserLose"), time.sleep(1.5)
                print ("< 201 >  PlayComplete"), time.sleep(1.5)

        elif (( p1 + p2 == 8 or p1 + p2 == 9 or p1 + p2 == 18 or p1 + p2 == 19 ) 
            and (b1 + b2 == 8 or b1 + b2 == 9 or b1 + b2 == 18 or b1 + b2 == 19 )) :
            p = p1 + p2 
            b = b1 + b2 
            if (p >= 10 and p < 20) :
                p = p - 10
        
            if (b >= 10 and b < 20) :
                b = b - 10

            vsPoint = checkpoint(p,b)
            if (vsPoint == "player") :
                notice = "Player Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'p' or bet == 'P') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "draw") :
                notice = "Draw"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'D' or bet == 'd') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete") , time.sleep(1.5) 
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)
            
            elif (vsPoint == "banker") :
                notice = "Banker Win"
                serverSocket.sendto(notice.encode(), clientAddress)
                if (bet == 'B' or bet == 'b') :
                    money[IDplayer - 1] = money[IDplayer - 1] + moneyTobet
                    message = "You earn money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 204 >  UserWin"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete"), time.sleep(1.5)  
                else :
                    money[IDplayer - 1] = money[IDplayer - 1] - moneyTobet
                    message = "You loss money " + str(moneyTobet)
                    serverSocket.sendto(message.encode(), clientAddress)
                    serverSocket.sendto(str(money[IDplayer - 1]).encode(), clientAddress)
                    print ("< 205 >  UserLose"), time.sleep(1.5)
                    print ("< 201 >  PlayComplete") , time.sleep(1.5)   
                
                        

    # num = num + 1
    # print (num)
    #message, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode().upper()
    # serverSocket.sendto(modifiedMessage.encode(), clientAddress)