import random


def split(word):
    return[char for char in word]

output = []

def removenestings(l):
    for i in l:
        if type(i) == list:
            removenestings(i)
        else:
            output.append(i)
    return output

def encryption(lines):
    cipherlist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ourlist = lines.split()
    ourlist2 = []
    charlist = []
    n = 0
    for i in ourlist:
        ourlist2.append(split(ourlist[n]))
        n = n+1
    charlist = removenestings(ourlist2)
    print(ourlist2)
    p = 0 
    q = 0
    newlist = []
    for i in charlist:
        p = 0
        for j in cipherlist:
          if charlist[q] == cipherlist[p]:
             newlist.append(cipherlist[p+3])
          p += 1
        q += 1

    print(newlist) 
    print(charlist)
    
    
print('Enter the line you want to encrypt EXCEPT CHARS XYZ')
line = str(input()).upper()
print(line)
print('The encrypted line will be:')
encryption(line)