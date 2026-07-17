"""
Question 3 (Instance Methods)

Create a class named BankAccount.

Requirements

Use the __init__() constructor.

The class should have these instance variables:
- account_holder
- account_number
- balance

Create these methods:

- deposit(amount)
  Add the amount to the balance.

- withdraw(amount)
  If the balance is enough, subtract the amount.
  Otherwise, print "Insufficient Balance".

- display()
  Print the account holder name, account number, and current balance.

Create 2 bank account objects.

Perform at least:
- One deposit
- One successful withdrawal
- One unsuccessful withdrawal

Finally, display the account details.
"""

class BankAccount():
    
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        
    def deposit(self, ammount):
        self.balance += ammount
        print(f"The ammount {ammount} has successfully deposited...")
    
    def withdraw(self, ammount):
        if ammount <= self.balance:
            self.balance -= ammount
            print(f"The amount {ammount} has withdrawed successfully...")
        else:
            print(f"insufficient bank balance...!")
            
    def display(self):
        print(f"Account holder name is {self.account_holder}")
        print(f"Account number is {self.account_number}")
        print(f"Current bank balance is {self.balance}")
        print()
        
customer1 = BankAccount("Suraj rajesh Lohar", 656486646, 20000)
customer2 = BankAccount("Vishwas Sudhir vedpathak", 345876346, 35000)

customer1.deposit(7500)
customer1.display()
customer2.withdraw(3000)
customer2.display()
customer1.withdraw(117500)
customer1.display()
'''
The ammount 7500 has successfully deposited...
Account holder name is Suraj rajesh Lohar
Account number is 656486646
Current bank balance is 27500

The amount 3000 has withdrawed successfully...
Account holder name is Vishwas Sudhir vedpathak
Account number is 345876346
Current bank balance is 32000

insufficient bank balance...!
Account holder name is Suraj rajesh Lohar
Account number is 656486646
Current bank balance is 27500
'''
