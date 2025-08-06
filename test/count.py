string=input("enter the string: ")
oldchar = string[0]
count=1
for i in range(1,len(string)):
    if string[i]==oldchar:
        count=count+1
    else:
        print(oldchar,count)
        oldchar=string[i]
        count=1
    if(i==len(string)-1):
        print(oldchar,count)
