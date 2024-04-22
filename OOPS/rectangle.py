class rectangle:
    def __init__(self,num1,num2):
        self.length = num1
        self.breadth = num2
        self.perimeter()

    def perimeter(self):
        peri  = self.length+self.breadth
        return peri*2
    def area(self):
        air = self.length*self.breadth
        return air
    def __str__(self):
        return "The length of rectangle is: {}\nThe breadh of rectangle is: {}\nPerimeter of rectangle is: {}\nArea of rectangle is: {} ".format(self.length,self.breadth,self.perimeter(),self.area())
meow = rectangle(3,4)
print(meow)