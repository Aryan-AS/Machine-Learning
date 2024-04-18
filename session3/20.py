# s = str(input("Enter the string"))
# meow = []
# woof = ''
# for i in s:
#  meow.append(i)a
# print(meow)
# for i in s:
#    print("start of i")
#    print(i)
#    for j in meow:
#      print("start of j")
#      print(j)
#      if(i!=j):
#        woof = woof + j

# print(woof)

# Code here
s = 'aaaabbbbbccccdddeeeeffff'

res = ''

for i in s:
  if i not in res:
    res = res + i

print(res)