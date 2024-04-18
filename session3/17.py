s = str(input("Enter the string"))
woof = ' '
meow = []
for i in s.split():
    meow.append(i)
print(meow)
for i in range(len(meow),0,-1):
   woof = woof +" "+ meow[i-1]

print(woof)



