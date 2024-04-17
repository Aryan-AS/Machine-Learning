a = int(input("Enter an integer"))
number = a 
result = 0

while number>0:
 modu = number%10
 result = result*10 + modu
 number = number//10
print(result)

    

