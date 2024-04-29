from abc import ABC,abstractmethod

class Polygon(ABC):

    def __init__(self,length,breadth,width):
        self.length = length
        self.breadth = breadth
        self.width = width
    
    def area(self):
        pass
class Rectangle(Polygon):
    def area(self):
        return self.length*self.width
    
class Triangle(Polygon):
    def area(self):
        return (self.length*self.breadth)*0.5

meow = Rectangle(1,2,3)
woof = Triangle(1,2,3)
print(meow.area())
print(woof.area())