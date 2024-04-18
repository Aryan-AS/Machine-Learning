list1 = [2,4,6,10,1]
sum = 0
list2=[]
for i in list1:
    sum = i
    for j in list1:
        if i<j:
            sum = sum + j
    list2.append(sum)
print(list2)