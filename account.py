class Account:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        #the self is the super-parameter and the name and balance attached to them are the sub-parameters.
    
    def deposit(self, amount):
        # the self and amount are parameters that we pass in the def function
        self.balance += amount
        #the += amount is the addition that is going to be done when the user makes a deposit

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            print("Insufficient Balance")
            return False
        
    def get_balance(self):
        return self.balance
    
