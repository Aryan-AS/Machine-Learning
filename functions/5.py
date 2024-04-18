number = 6
def perfect(number):
    sum1 = 0
    for i in range(1,number):
        if number%i==0:
            sum1 = sum1 + i

    if sum1 == number:
      
      return "It is a perfect number"

print(perfect(number))

