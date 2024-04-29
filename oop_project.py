from bank_accounts  import * # type: ignore


Dave = BankAccount(1000, 'Dave') # type: ignore
Sarah = BankAccount(1000, 'Sarah')
Ronen = BankAccount(1000000, 'Ronen')

Ronen.getBalance()
Dave.getBalance()
Sarah.getBalance()

Sarah.deposit(1000000)
Dave.deposit(500)

Dave.Withdraw(10000)
Sarah.Withdraw(1000000)

Ronen.Transfer(100 , Dave)
Sarah.Transfer(2000000, Ronen)