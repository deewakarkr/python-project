string=input("enter your string: ")
for i ,c in enumerate(string):
    found=False
    for j ,ic in enumerate(string):
        
        if i!=j and c ==ic:
            found=True
            break
    if found==False:
        print(f"your non repeation { c}")
        break
        
        

