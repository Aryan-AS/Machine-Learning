list1=[1,2,3,4,5,1]
list2=[2,3,5,7,8]
list3 =[]
for i in list1:
 if i not in list3:
  list3.append(i)
for j in list2:
 if j not in list3:
  list3.append(j)

print(list3)
       
    

