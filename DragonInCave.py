import time


def intro():
    print('''You are in a land full of Dragons. In front of you,
 you see two caves. In one cave, the dragon is friendly
 and will share his treasure with you. the other dragon 
 is greedy and hungry and will eat you on sight.
 Which cave will you go into? (1 or 2)''') 


def cavechosen():
    print("Enter the Number of the cave you want to enter")
    num = int(input())
    return num

def ResultAfterChoosing(cavechosen):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    time.sleep(3)
    
    if cavechosen == 1:
        print("And will Give the Treasures")
    else:
        print("Will Gobble you in one bite")

intro()
val = cavechosen()
ResultAfterChoosing(val)


