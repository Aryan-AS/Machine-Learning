# Code here
n = int(input('enter the number of terms'))

start = 2
sum = 0

for i in range(0,n):
  if i < n-1:
    print(start,end='+')
  else:
    print(start)

  sum = sum + start
  start = start*10 + 2

print(sum)