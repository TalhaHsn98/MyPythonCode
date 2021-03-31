import random
print("Hello!!! What is your name")
name = str(input())
print(name)
randnumber = random.randint(1,20)
n = 1
while n <= 5:
  print("Hey " +name+ " Guess a number between 1 to 20")
  guessednum = int(input())
  if guessednum == randnumber:
      print("You Got it correct")
      print(guessednum)
      print("You Won")
      break
  elif guessednum < randnumber:
      print('You got it wrong')
      print(guessednum)
      print('Go Higher')
      n = n + 1
  elif guessednum > randnumber:
      print("You got it wrong")
      print(guessednum)
      print("Go Lower")
      n = n + 1

if n > 5:
    print('You lose')
    