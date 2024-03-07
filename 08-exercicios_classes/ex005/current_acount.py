class current_acount:
    
    def __init__(self, acount_number, name, balance = 0):
        self.acount_number = acount_number
        self.name = name
        self.balance = balance

    def change_nome(self, newName):
        self.name = newName

    def cash_deposit(self, money):
        if money > 0:
            self.balance += money
        else:
            print("invalid value")

    def withdraw_money(self, money):
        if money >= self.balance:
            self.balance -+ money
        else:
            print("valor not found")
    