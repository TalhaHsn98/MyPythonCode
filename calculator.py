def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("Select operation 1,2,3,4")
print("1 - add")
print('2 - sub')
print('3 - mul')
print('4 - div')
choice = input(print("Enter 1/2/3/4"))
#num1 = print(input('Enter first numbers'))
#num2 = print(input('Enter second numbers'))

if choice in ('1','2','3','4'):
    num1 = int(input('Enter first numbers'))
    num2 = int(input('Enter second numbers'))
    if choice == '1':
        print(add(num1,num2))
    elif choice == '2':
        print(sub(num1,num2))
    elif choice == '3':
        print(mul(num1,num2))
    elif choice == '4':
        print(div(num1,num2))
else:
    print("invalid number entered")
