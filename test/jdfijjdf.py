def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return"error"
    return x/y
print("1. press 1 for add")
print("2. press 2 for sub")
print("3. press 3 for mult")
print("4. press 1 for div")
print("press any number1/2/3/4")
inte=int(input("enter the operation: "))
num1=int(input("enter the 1st num: " ))
num2=int(input("enter the 2nd num: "))
match inte:
    case 1: print(f"your addition is {add(num1,num2)}")
    case 2: print(f"your addition is {sub(num1,num2)}")
    case 3: print(f"your addition is {mult(num1,num2)}")
    case 4: print(f"your addition is {div(num1,num2)}")
    case _:print("invalid")