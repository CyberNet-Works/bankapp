class BalanceException(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)
        
class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\n${amount} Deposit to Account '{self.name}' complete.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nError, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def Withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print(f"\${amount} withdrawal from account '{self.name}' complete.")
            self.getBalance()
            
        except BalanceException as error:
            print(f"n${amount} withdrawal from Account '{self.name}' interrupted: {error}")
    
    def Transfer(self, amount, receiver_account):
        try:
            print(f"\n**********\n\nBeginning ${amount} transfer from '{self.name}' to '{receiver_account.name}' ..🚀")
            self.viableTransaction(amount)
            self.Withdraw(amount)
            receiver_account.deposit(amount)
            print(f"\n${amount} transfer from account '{self.name}' to receiver account '{receiver_account.name}' complete! ✅\n\n*********")
        except BalanceException as error:
            print(f"\n${amount} transfer from acount '{self.name}' to receiver account '{receiver_account.name}' interrupted ❌ {error}")
