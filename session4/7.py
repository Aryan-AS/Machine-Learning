list1 = ['1ac21', '23fg', '456', '098d','1','kls']
list2=[]
list3 = []
name = 0
product = 1
for i in list1:
    product =1
    name = i 
    for j in i:
    
        if j.isdigit():
            product = product*int(j)
    list2.append(product)
    list3.append(name)
print([i[1] for i in sorted(list(zip(list2,list3)),reverse=True)])
