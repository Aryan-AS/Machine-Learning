class Car:
    counting = 0
    def __init__(self):
        self.meow = Car.counting
        Car.counting =Car.counting +1




maruti = Car()
bmw = Car()
honda = Car()
print(Car.counting)