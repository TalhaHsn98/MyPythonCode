import random

def drawboard(Board):

    print(Board[7] +'|'+ Board[8] +"|"+ Board[9])
    print('-+-+-')
    print(Board[4] +'|'+ Board[5] +"|"+ Board[6])
    print('-+-+-')
    print(Board[1] +'|'+ Board[2] +'|'+ Board[3])

def input_from_player():
    letter = ''
    print("Enter which letter you want X or O")
    while not (letter == 'X' or letter == 'O'):
        print("Enter which letter you want X or O")
        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return['O','X']

def who_goes_first():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'
def makeMove(board,letter,move):
    board[move] = letter

def iswinner(bo,le):
    return ((bo[7]==le and bo[8]==le and bo[9]==le)or
    (bo[4]==le and bo[5]==le and bo[6]==le)or
    (bo[1]==le and bo[2]==le and bo[3]==le)or
    (bo[1]==le and bo[4]==le and bo[7]==le)or
    (bo[2]==le and bo[5]==le and bo[8]==le)or
    (bo[3]==le and bo[6]==le and bo[9]==le)or
    (bo[3]==le and bo[5]==le and bo[7]==le)or
    (bo[1]==le and bo[5]==le and bo[9]==le))


def getboardcopy(board):
    boardcopy = []
    for i in board:
        boardcopy.append(i)
    return boardcopy

def isspacefree(board,move):
    return board[move] == ' '

def getplayermove(board):
    move = ' '
    while move not in '1,2,3,4,5,6,7,8,9'.split() or not in isspacefree(board,int(move)):
        print('Enter your next move form(1-9)')
        move = input()
    return int(move)

def chooserandomMoveFromList(board,moveslist):
    possiblemoves = []
    for i in moveslist:
        if isspacefree(board,i):
            possiblemoves.append(i)
    if possiblemoves != 0:
        return random.choice(possiblemoves)
    else:
        return None

def getComputerMove(board,ComputerLetter):
    playerLetter = ' '
    if ComputerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    for i in range(1,10):
        boardcopy = getboardcopy(board)
        if isspacefree(boardcopy,i):
            makeMove(boardcopy,ComputerLetter,i)
            if iswinner(boardcopy,ComputerLetter):
                return i
    
    for i in range(1,10):
        boardcopy = getboardcopy(board)
        if isspacefree(boardcopy,i):
            makeMove(boardcopy,ComputerLetter,i)
            if iswinner(boardcopy,ComputerLetter):
                return i

    move = chooserandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    if isspacefree(board,5):
        return 5
    
    return chooserandomMoveFromList(board,[2,4,6,8])



def isBoardfull(board):
    for i in range(1,10):
        if isspacefree(board,i):
            return False
    return True


print("welcom To the TicTactoe")