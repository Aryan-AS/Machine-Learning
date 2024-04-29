class Bill:
    def __init__(self,item_price, items):
        self.__total = 0
        self.__items = items
        self.__price = item_price

        for i in self.__price:
            self.__total = self.__total +1
    def display_bill(self):
     
     for i in range(len(self.__items)):
        print(self.__price[i],"is", self.__items[i])
     print("Total Bill =",self.__total)

   