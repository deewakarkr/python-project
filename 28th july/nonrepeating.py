string=input("enter the character: ")
for i,c in enumerate(string):
    found=False
    for j,ic in enumerate(string):
        if i!=j and c==ic:
            found=True
            break
    if not found:
        print(c)
        break