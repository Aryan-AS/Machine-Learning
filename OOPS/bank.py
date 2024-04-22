class Bank:
    def __init__(self,a,b,c):
        self.accountnumber = int(a)
        self.name = str(b)
        self.balance = int(c)
    def display(self):
        print("Account Number",self.accountnumber)
        print("Account Name :",  self.name)
        print("Account Balance :",self.balance)
    def Deposit(self,amount):
        self.balance = self.balance + amount
    def Withdrawl(self,amount):
        if amount> self.balance:
            print("Insuffiencent balance")
        else:
            self.balance = self.balance - amount
            reduction = self.bankfees()
            self.balance = self.balance - reduction
    def bankfees(self):
        return 0.05*self.balance
meow = Bank(69420,"Aryan",1000000)
meow.Withdrawl(500)
meow.Deposit(1000)
meow.display()