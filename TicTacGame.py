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

