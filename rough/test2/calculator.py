def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    if y==0:
        return"error"
    return x//y
while True:
    print("1. press 1 for add")
    print("2. press 2 for add")
    print("3. press 3 for add")
    print("4. press 4 for add")
    print("5. press any key to exit")
    choice = input("Enter your choice: ")
    try:
        choice=int(choice)
    except Exception as e:
        print("enter a valid numbchoicer")
        continue
    a=input("enter your 1st number")
    try:
        a=int(a)
    except Exception as e:
        print("enter a valid number")
        continue
    b=input("enter your 2nd number")
    try:
        b=int(b)
    except Exception as e:
        print("enter a valid number")
        continue
    match choice:
        case 1 : print("your result is",add(a,b))
        case 2 : print("your result is ",sub(a,b))
        case 3 : print("your result is ",mult(a,b))
        case 4 : print("your result is ",div(a,b))
        case _: break
print("efwvhdvs")