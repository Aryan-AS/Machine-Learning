list1= [[1,2,3],[4,5,6],[7,8,9]]
list2 = []
sum = 0
for i in list1:
    sum = 0
    for j in i:
        if sum<j:
         sum = j
    list2.append(sum)
print(list2)
    
