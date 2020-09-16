#AUTHOR#SUDHANVA PATURKAR
#TIC-TAC-TOE PROBLEM using MINIMAX Algorithm 
def printBoard(board):
    print("-------")
    print("|"+board[0]+"|"+board[1]+"|"+board[2]+"|")
    print("|-----|")
    print("|"+board[3]+"|"+board[4]+"|"+board[5]+"|")
    print("|-----|")
    print("|"+board[6]+"|"+board[7]+"|"+board[8]+"|")
    print("-------")
    
def getBoards(board,turn):
    boards=[]
    for i in range(9):
        if board[i]=='-':
            temp= board.copy()
            temp[i]='X' if turn==1 else 'O'
            boards.append(temp.copy())
    return boards

def getNextTurn(currentBoard ,turn):
        pB={}

        possibleTurns=getBoards(currentBoard,turn)
        for b in possibleTurns:
            stat=isWinner(b)
            if stat=='X':
                val=1*(b.count('-')+1)
                pB[int(val)]=b
            elif stat=='O':
                val=-1*(b.count('-')+1)
                pB[int(val)]=b
            elif stat=='-':
                pB[int(0)]=b
            else:
                if b.count('-')!=0:
                    temp,val=getNextTurn(b,0 if turn==1 else 1)
                    pB[int(val)]=b 
        if turn==1:
            val=max(pB)
            return pB[val],val
        else:
            val=min(pB)
            return pB[val],val


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
    w=isWinner(board)
    if w=='O':
        print('You WIN!')
        win=1
    elif w=='-':
        print('Its a DRAW!')
        win=1
    elif w=='X':
        print('AI WINS!')
        win=1
    else:
        turn=1
        board,val=getNextTurn(board,turn)
        printBoard(board)
        w=isWinner(board)
        if w=='X':
            print("AI wins!")
            win=1
        elif w=='-':
            print("Its a DRAW!")
            win=1
        
