class computer:
    def __init__(self):
       pass
    def factorial(self,n):
       factorial = 1

       if n < 0:
          return "Invalid"
       elif n == 0:
          return 1
       else:
          for i in range(1,n + 1):
               factorial = factorial*i
          return factorial
    def naturalsum(self,n):
     sum = 0
     for i in range(1,n+1):
          sum = sum + i
     print(sum)
    def testPrime(self,n):
     if n == 1:
        return "prime"
     for i in range(2,n):
       if n%i==0:
          return "not prime"
       else:
          return "prime"
    def testprims(self,n1,n2):
       list1 = []
       list2 = []
       for i in range(1,n1):
          if n1%i==0:
             list1.append(i)
       for i in range(1,n2):
          if n2%i==0:
             list2.append(i)
             
       meow = set(list1,list2)
       if meow == {1}:
          return "It is prims"
       else:
          return "It is not prims"
       
aryan = computer()
aryan.factorial(6)
aryan.naturalsum(7)


       

    
          
    
  