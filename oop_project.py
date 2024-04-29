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

Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.Transfer(100, Dave)

Johnson = SavingsAccount(1000, "Johnson")

Johnson.getBalance()

Johnson.deposit(100)

Johnson.Transfer(10000, Sarah)

Johnson.Transfer(1000, Sarah)

Johnson.Withdraw(1)