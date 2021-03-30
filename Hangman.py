import random
print('Bis')
#Hangman list for pictorial representation of the Game
HangmanPics = ['''
+---+
    |
    |
    |
   ===''','''
+---+
O   |
    |
    |
   ===''','''
+---+
O   |
|   |
    |
   ===''','''
 +---+
 O   |
/|   |
     |
    ===''','''
 +---+
 O   |
/|\  |
     |
    ===''','''
 +---+
 O   |
/|\  |
/    |
    ===''','''
 +---+
 O   |
/|\  |
/ \  |
    ==='''
]
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk  lion lizard llama mole monkey moose mouse mule newt otter owl panda'.split()

#Generating a random word from list of words using randint and random
def Getrandomword(wordlist):
    wordindex = random.randint(0,len(wordlist)-1)
    return wordlist[wordindex]

#Function for displaying the board
def DisplayBoard(missedletters,correctletters,secretword):
    print(HangmanPics[len(missedletters)])
    print("Missed Letters", end = ' ')
    for letter in missedletters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretword)

    for i in range(len(correctletters)):
        if secretword[i] in correctletters:
            #blanks list is first printed till i then the correct word is written then
            #again the blanks are printed
            blanks = blanks[:i] + secretword[i] + blanks[i+1:]
    for letter in blanks:
        print(letter , end = ' ')
    print()

#getting the guess from the Player
def getguess(alreadyguessed):
    while True:
        print('Enter the Guessing letter:')
        Guess = input()
        Guess = Guess.lower()
        if len(Guess)>1:
            print("Enter only a single letter")
        elif Guess in alreadyguessed:
            print("you already guessed this letter")
        elif Guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Invalid entry MFc")
        else:
            return Guess

        
#check if user wants to play again
def Playagain():
    print('Do you want to play the Game agian yes or no')
    return input().lower().startswith('y')

print('H A N G M A N')
correctletters = ''
missedletters = ''
secretword = Getrandomword(words)
gamedone = False


while True:
    DisplayBoard(missedletters,correctletters,secretword)

    guess = getguess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess
        foundallletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundallletters = False
                break
        if foundallletters:
            print("yes the secret word is " + secretword + " you won")
            gamedone = True
    else:
        missedletters = missedletters + guess
        if len(missedletters) == len(HangmanPics) - 1:
            DisplayBoard(missedletters,correctletters,secretword)
            print("Number of missed guesses:" +str(len(missedletters))+"Number of correct guessses:" +str(len(correctletters))+"The secret word:"+secretword+' ')
            gamedone = True
        
    if gamedone:
        if Playagain:
            missedletters = ' '
            correctletters = ' '
            secretword = getguess(words)
            gamedone = False
        else:
            break