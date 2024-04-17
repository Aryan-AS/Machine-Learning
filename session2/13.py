a = int(input("Input the number"))
woof = a
number = 0
meow = 0
sum = 0
while a>0:    
    meow = a%10
    sum = sum + pow(meow,3)
    
    a = a//10


print(sum)
if sum ==woof:
    print(True)

else:
    print(False)    