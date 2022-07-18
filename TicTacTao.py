gameTable=[num for num in range(0, 10)]
indicator=0
player_1=str()
player_2=str()


def printTable(gameTable_):
    for i in range(0, len(gameTable_), 3):
        print( " | ",gameTable_[i], " | ", gameTable_[i+1], " | ", gameTable_[i+2], " | ")

def choiceEntering():
    global indicator
    if(indicator%2):
        player=player_2
    else:
        player=player_1
    while True:
        print(player ,", Enter your choice :")
        choice=int(input())
        if choice in gameTable:
            if indicator%2==0 :
                gameTable[choice-1]='X'
            else:
                gameTable[choice-1]='O'
            indicator+=1
            break
        else :
            print("Please choose an empty spot.")

def checkWinner():
    if gameTable[0]==gameTable[1]==gameTable[2]:
        return True
    
    if gameTable[3]==gameTable[4]==gameTable[5]:
        return True
   
    if gameTable[6]==gameTable[7]==gameTable[8]:
        return True
   
    if gameTable[0]==gameTable[3]==gameTable[6]:
        return True
    
    if gameTable[1]==gameTable[4]==gameTable[7]:
        return True
    
    if gameTable[2]==gameTable[5]==gameTable[8]:
        return True
    
    if gameTable[0]==gameTable[4]==gameTable[8]:
        return True
    
    if gameTable[2]==gameTable[4]==gameTable[6]:
        return True

    return False



gameTable=[num for num in range(1, 10)]

print(" Welcome to Tic Tac Tao ! ")
print(" Player 1 'X' : ")
player_1=input()
print(" Player 2 'O' : ")
player_2=input()


while True:

    print("")
    printTable(gameTable)
    choiceEntering()
    if checkWinner():
        printTable(gameTable)
        if indicator%2!=0:
            print("Congrats, ", player_1, " is the winner.")
        else :
            print("Congrats, ", player_2, " is the winner.")
        break
    elif indicator==9:
        printTable(gameTable)
        print("Thats a draw !")
        break
