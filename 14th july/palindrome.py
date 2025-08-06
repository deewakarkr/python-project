num = int(input("Enter the number"))
original = num
reverse = 0
while num > 0:
    digit = num%10
    reverse = (reverse*10)+digit
    num//=10
if original == reverse:
    print("the number is palindrome")
else:
    print("the number is not palindrome")

