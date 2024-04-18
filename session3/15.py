s = str(input("Enter the string"))
meow = ''
for i in s:
    if i.isdigit():
        meow =  meow + i

print(meow)