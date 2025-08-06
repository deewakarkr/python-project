def y(string):
    for char in string:
            if string.count(char) ==1:
                return char
            return None
string=input("enter a string")
result = y(string)
if result:
   print("first non repeating character is ",result)
else :
    print("non repeating character is not available")