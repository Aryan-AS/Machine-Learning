meow = "hello how are you i am fine thank you"
def high(meow):
  temp = 0
  max = 0
  woof = 0
  for i in  meow.split():
    for j in meow.split():
      if i == j:
        temp = temp + 1
  if max<temp:
    woof = i
    max = temp
  return woof
print(high(meow))