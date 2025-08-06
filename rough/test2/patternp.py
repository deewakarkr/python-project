# dimond
row=6
for i in range(row):
    for j in range(row-1-i):
        print("#",end="")
    print()
    for j in range(i+1):
        print("*",end="")
    print()
