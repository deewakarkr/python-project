num=int(input("Enter your number"))
total =0
n = num
power =len(str(num))
while n > 0:
	digit = n%10
	total =total+digit** power
	n//=10
if total == num:
	print("the number is armstrong")
else:
	print("the number is not armstrong")
		