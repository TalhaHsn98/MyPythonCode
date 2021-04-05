print('Caesar Cipher')

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
Max_size = len(SYMBOLS)


def getmode():
    print('Enter if you want to encrypt or decrypt')
    mode = input().lower()
    if mode in ['encrypt','e','decrypt','d']:
        return mode
    else:
        print('Enter either encrypt or e or decrypt or d')
        getmode()

def getmessage():
    print('Enter the message you want to en or de')
    return input()

def getkey():
    key = 0 
    while True:
        print('Enter the key you want between 1-52')
        key = int(input())
        if(key >= 1 and key <= Max_size):
            return key

def gettranslatedmessage(mode,message,key):
    if mode[0] == 'd':
        key = -key
    Translated = ' '

    for symbol in message:
        symbolindex = SYMBOLS.find(symbol)

        symbolindex += key

        if symbolindex >= len(SYMBOLS):
            symbolindex -= len(SYMBOLS)
        elif symbolindex < 0:
            symbolindex += len(SYMBOLS)
        
        Translated += SYMBOLS[symbolindex]
    return print(Translated)


mode = getmode()
message = getmessage()
key = getkey()

print("Your translated message is :")

gettranslatedmessage(mode,message,key)