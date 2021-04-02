import random

def provideIntro():
     print('''I am thinking of a 3 digit number. Try to guess what it is.
     The clues I give are ...
     When I say:         That means:
     1)Bagels            None of the digits is correct.
     2)Pico              One digit is correct but in the wrong position.
     3)Fermi             One digit is correct and in the right postion
     I have thought of a number. You have 10 guesses to get it.''')

def Getlistandshuffle(givenlist):
    random.shuffle(givenlist)
    return givenlist
    
# Generating a 3 digit number using Random 
def GetsecretKey():
     numberlist = list(range(10))
     #print(numberlist)
     listof10 = Getlistandshuffle(numberlist) 
     #print(listof10)
     secretkey = ''
     for i in range(3):
         secretkey += str(listof10[i])
     return secretkey

# Getting a 3 digit number in form of a string 
def Get_input_From_Player():
     print("Enter a Three digit number")
     numinformatofstr = str(input())
     if len(numinformatofstr) == 3:
         #print("Correct")
         return numinformatofstr
     else:
         print('Enter only a three digit')
         Get_input_From_Player()



def Comparing_Input_and_secrectkey():
  Secretkey = GetsecretKey()
  inputfromplayer = Get_input_From_Player()
  n = 0
  while n <= 5:
     if Secretkey == inputfromplayer:
          print("YOU WON!!!!!")
          break
     for i in range(len(inputfromplayer)):
        if inputfromplayer[i] == Secretkey[i]:
          print('Fermi')
        elif inputfromplayer[i] in Secretkey:
          print('Pico')
        elif inputfromplayer[i] != Secretkey[i]:
          print('Bagel')  
     inputfromplayer = Get_input_From_Player()
     n += 1
  if Secretkey != inputfromplayer:
      print('Sorry you lost the game')
      print('The Secret Key is:')
      print(Secretkey)



def Playagain():
  print("Do you want to play again")
  print('Enter y or n')
  play = str(input())
  if play == 'y':
    provideIntro()
    Comparing_Input_and_secrectkey()
  else:
    print('Bye bye Tc')

provideIntro()   
Comparing_Input_and_secrectkey()
Playagain()