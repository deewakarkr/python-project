char=(input("enter the string"))
oldchar=char[0]
count=1
for i in range(1,len(char)):
    if char[i]==oldchar:
        count=count+1
    else:
        print(oldchar, count)
        oldchar = char[i]
        count = 1
print(oldchar, count)
