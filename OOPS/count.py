class Point:
    def __init__(self,x,y):
        self.x1 = x
        self.x2 = y
    def __str__(self):
        return "<{},{}>".format(self.x1,self.x2)
    def eculudiandistance(self,other):
        return ((self.x1-other.x1)**2 + (self.x2-other.x2)**2)**0.5
    def fromorigin(self):
        return self.eculudiandistance(Point(0,0))
    

meow = Point(1,2)
woof = Point(2,4)
print(meow.eculudiandistance(woof))
print(meow.fromorigin())
