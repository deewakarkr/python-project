score =int(input("Enter your score: "))
grade ="A" if score>90 else "B" if score>80 and score<90 else "LOW" 
print(grade)