class computer:
    def __init__(self):
        pass

    def factorial(self, n):
        if n < 0:
            return "Invalid"
        elif n == 0:
            return 1
        else:
            factorial = 1
            for i in range(1, n + 1):
                factorial *= i
            return factorial

    def naturalsum(self, n):
        total = 0
        for i in range(1, n + 1):
            total += i
        return total

    def testPrime(self, n):
        if n < 2:
            return "not prime"
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return "not prime"
        return "prime"

    def testprims(self, n1, n2):
        list1 = [i for i in range(1, n1) if n1 % i == 0]
        list2 = [i for i in range(1, n2) if n2 % i == 0]
        
        common_factors = set(list1).intersection(list2)
        if common_factors == {1}:
            return "It is prims"
        else:
            return "It is not prims"

    def tableMult(self, n):
        return [n * i for i in range(1, 11)]

    def listDiv(self, n):
        listd = [i for i in range(1, n) if n % i == 0]
        return listd


aryan = computer()

print("Factorial of 6:", aryan.factorial(6))
print("Sum of natural numbers up to 7:", aryan.naturalsum(7))
print("Multiplication table of 6:", aryan.tableMult(6))
print("Is 5 a prime number?", aryan.testPrime(5))
print("Are 5 and 6 prime with each other?", aryan.testprims(5, 6))
print("Divisors of 5:", aryan.listDiv(5))

    
          
    
  