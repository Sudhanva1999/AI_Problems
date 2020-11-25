#AUTHOR#SUDHANVA PATURKAR
#TIC-TAC-TOE PROBLEM using Heuristic Search(Steepest Ascend Hill Climbing)
def printBoard(board,hval):
    print("-------")
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|-----|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|-----|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")
    print("-------")
    print("H-VALUE="+str(hval))
    print("-------")

def isWinner(board):
    lists1=[]
    temp=board.copy()
    for i in [0,3,6]:
        lists1.append(temp[i:i+3])
    lists1=lists1+list(map(list, zip(*lists1))) 
    lists1.append([temp[0],temp[4],temp[8]])
    lists1.append([temp[2],temp[4],temp[6]])
    for i in lists1:
            x=i.count("X")
            o=i.count("O")
            b=i.count("-")
            if(x==3):
                return 'X'
            if(o==3):
                return 'O'
    if (board.count("-")==0):
        return '-'
    else:
        return '--'

    
def getHeuristic(temp):
    lists=[]
    sum=0
    for i in [0,3,6]:
        lists.append(temp[i:i+3])
    lists=lists+list(map(list, zip(*lists))) 
    lists.append([temp[0],temp[4],temp[8]])
    lists.append([temp[2],temp[4],temp[6]])

    for i in lists:
        x=i.count("X")
        o=i.count("O")
        b=i.count("-")
        if(x==3):
            sum+=1000
        elif(x==2 and b==1):
            sum+=10
        elif(x==1 and b==2):
            sum+=1
        elif(o==3):
            sum-=1000
        elif(o==2 and b==1):
            sum-=100
        elif(o==1 and b==2):
            sum-=1
        elif(b==3 or (x==1 and o==1)):
            sum+=0
    return sum


def getNextTurn(currentBoard):
    possibleBoards={}
    for i in range(9):
        if currentBoard[i]=='-':
            temp= currentBoard.copy()
            temp[i]='X'
            hv= getHeuristic(temp)
            possibleBoards[hv]=temp
    resTurn=[]
    Mhv=-9999
    for y,x in possibleBoards.items():
        # print("----------------------")
        # printBoard(x,y)
        # print("----------------------")
        if y>Mhv:
            Mhv=y
            resTurn=x
    return resTurn,Mhv
    
board=["-","-","-","-","-","-","-","-","-"]
win=0
print("Please Enter position where you want to place Your mark.('O')")
while(win==0):
    print("Enter Position:")
    pos=int(input())-1
    if board[pos]!="-":
        print("Invalid Position")
        continue
    board[pos]="O"
    if board.count("-")==0:
        print("DRAW!")
        win=2
    else:
        board,hv=getNextTurn(board)
        printBoard(board,hv)
        w=isWinner(board)
        if w=='X':
            print("AI wins!")
            win=1
        elif w=='O':
            print("YOU Win!")
            win=1
        elif w=='-':
            print("its a DRAW!")
            win=1
