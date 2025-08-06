num=int(input("enter the number"))
revese=0
original=num
while num!=0:
    digit=num%10
    revese=(revese*10)+digit
    num=num//10
if original== revese:
    print("the number is palindrom")
else:
    print("the number is not palindrom ")

