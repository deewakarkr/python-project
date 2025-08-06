string=input("enter the string: ")#deewakar
d={}
for x in string.lower():
    if x not in d:
        d[x]=1
    else:
        d[x]+=1
print(d)
    