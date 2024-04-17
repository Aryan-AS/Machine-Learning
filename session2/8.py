a = int(input("Enter a number"))
i = 0
meow = 0
while i<a+1:
  i = i +1
  if(i%5!=0):
   meow = meow +i
  if(meow>=300):
    break

print(meow)


