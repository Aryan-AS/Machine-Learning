meow = [[1, 2, 2, 4, 3, 6],
 [5, 1, 3, 4],
 [9, 5, 7, 1],
 [2, 4, 1, 3]]
woof = set()
 
for i in meow:
    for j in i:
      woof.add(j)

print(woof)        