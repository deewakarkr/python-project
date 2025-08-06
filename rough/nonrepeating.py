string=input("enter the string: ")
for c in string:
    if string.count(c)==1:
        print(c)
        break
else:
    print("there is no non repeation character ")