string=input("enter the string: ")
print("operation to perfome 1.total length 2. count of character")
choice=input()
if choice=="1":
    print(len(string))
elif choice=="2":
    char= input("enter character : ")
    if char in string:
        print(string.count(char))
    else:
        print("charactet not avalible.")
else:
    print("invalid choice.......")