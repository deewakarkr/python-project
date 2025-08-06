
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "error"
    return x/y
while  True:
    print("1. press 1 for addition ")
    print("2. press 2 for subtraction ")
    print("3. press 3 for multiplication ")
    print("4. press 4 for division ")
    print("5. press 5 for quit")
    choice = input("Enter your choice: ")
    if choice in ['1','2','3','4']:
        choice = int(choice)
    else:
        break
    num1 = input("Enter first number: ")
    try:
        num1 =int(num1)
    except Exception as e:
        print("Enter a valid number")
        continue
    num2 = input("Enter second number: ")
    try:
        num2= int(num2)
    except Exception as e:
        print("Enter a valid number")
        continue
    match choice:
        case 1: print("your summation is ",add(num1,num2))
        case 2: print("your subtraction is ",subtract(num1,num2))
        case 3: print("your multiplication is ",multiply(num1,num2))
        case 4: print("your division is ",divide(num1,num2))
        case _: break
print("see you again")

