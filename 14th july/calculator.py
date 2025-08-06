def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	if y == 0:
		return "error"
	return x/y
print("1. for add")
print("2. for sub")
print("3. for mult")
print("4. for div.")
print("enter your choice 1/2/3/4")
choice =input("Enter your choice")
num1 = int(input("Enter your 1st number"))
num2 = int(input("Enter your 2nd number"))
match choice :
	case '1' : print(f"your result is :{add(num1,num2)}")
	case '2' : print(f"your result is :{sub(num1,num2)}")
	case '3' : print(f"your result is :{multiply(num1,num2)}")
	case '4' : print(f"your result is :{divide(num1,num2)}")
	case _ : print("invalid input")
		
	
	
		