import math
i = int(input("Enter a number"))
result = 0
for j in range(0,i+1,1):
    if(j==0):
     result = result +1
    else:
       result = result + pow(result,i/i)

print(result)
