class Vehicle:
     def __init__(self,seat):
          self.seat = seat
    
     
     def fare_charge(self):
         return 100*self.seat
    
          
    
    



class Bus(Vehicle):
   def fare_charge(self):
       fare = 100*self.seat
       return fare+(0.1*fare)
   

meow = Bus(50)
print(meow.fare_charge())
       