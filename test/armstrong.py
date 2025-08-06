num=int(input("enter the number"))
original=num

reverse=0
power =len(str(num))
while num!=0:
    digit=num%10
    reverse=reverse+digit** power
    num=num//10
if reverse== original:
    print("the number is armstrong") 
else:
    print("the number is not armstrong")

