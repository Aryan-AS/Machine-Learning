moo = (1, 5, 7, 8, 10)
meow = list(moo)
woof = []
sum = 1
for i in range(0,len(meow)):
    sum  = 1
    if i == 0:
        sum = sum*meow[i]*meow[i+1]
        woof.append(sum)
    sum = 1
    if i!=0 and i!=-1 and i!=len(meow)-1:
        sum = sum*meow[i-1]*meow[i]+meow[i]*meow[i+1]
        woof.append(sum)
    
    sum = 1
    if i ==len(meow)-1:
        sum = sum*meow[i]*meow[i-1]
        woof.append(sum)
print(tuple(woof))

    
