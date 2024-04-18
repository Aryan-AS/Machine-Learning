a = str(input("Input a number"))
a = list(a)
count = 0
meow = []
for i in a:
    if i not in meow:
        meow.append(i)
        count = count + 1

if count>2:
    print("Not Binary")
else:
    print("Binary")