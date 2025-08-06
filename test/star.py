star=int(input("enter the number of star"))
for i in range(star):
    for j in range(star-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(star-1):
    for j in range(i+1):
        print(" ",end="")
    for j in range(star-i-1):
        print("* ",end="")
    print()
    
