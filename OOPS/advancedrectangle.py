class Rectangle:
    def __init__(self,length,height):
        self.height = height
        self.length = length
    @classmethod
    def property(cls,len,hei):
        return cls(len,hei)
    
    def area(self):
        return self.height * self.length
    def issquare(self):
        return "It is a square" if self.height == self.length else "It is not a square"

meow = Rectangle.property(1,2)
print(meow.area())
print(meow.issquare())