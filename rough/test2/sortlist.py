list1=[1,3,10,5]
list2=[2,4,8,6]
list1.sort()
list2.sort()
i,j = 0,0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        i<len(list1) 
        print(list1[i])
        i=i+1
    else:
        print(list2[j])
        j=j+1
while i<len(list1):   
    print(list1[i])
    i+=1
while i<len(list2):
    print(list2[j])
    j+=1

