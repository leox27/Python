"""
#6. (Advanced Abstraction - Payment System)

Create an abstract class named Payment.
Requirements
Use ABC and abstractmethod.

Create a constructor that stores:
- amount
Create a normal method:
- display_amount()

It should print the payment amount.
Create two abstract methods:
- process_payment()
- generate_receipt()

Create three child classes:
- CreditCardPayment
- UPIPayment
- CashPayment

CreditCardPayment:
- process_payment() should print:
  "Processing Credit Card payment"
- generate_receipt() should print:
  "Credit Card receipt generated"

UPIPayment:
- process_payment() should print:
  "Processing UPI payment"
- generate_receipt() should print:
  "UPI receipt generated"

CashPayment:
- process_payment() should print:
  "Processing Cash payment"
- generate_receipt() should print:
  "Cash receipt generated"

Create one object of each payment class.
Call:
- display_amount()
- process_payment()
- generate_receipt()
Do not use if-else to identify the payment type.
"""

from abc import ABC, abstractmethod

class Payment(ABC):
    
    def __init__(self, amount):
        self.amount = amount
        
    def display_amount(self):
        print(f"Amount is {self.amount}")
        
    @abstractmethod
    def process_payment(self):
        pass
    
    @abstractmethod
    def generate_payment(self):
        pass
    
class CreditCardPayment(Payment):
    
    def process_payment(self):
        print("Processing Credit Card payment")
    
    def generate_payment(self):
        print("Credit Card receipt generated")
        
class UPIPayment(Payment):
    
    def process_payment(self):
            print("Processing UPI Card payment")
        
    def generate_payment(self):
        print("UPI receipt generated")
            
class CashPayment(Payment):
    
    def process_payment(self):
            print("Processing Credit Card payment")
        
    def generate_payment(self):
        print("Cash receipt generated")
        
creditcard1 = CreditCardPayment(10000)
upi1 = UPIPayment(7000)
cash1 = CashPayment(3000)

creditcard1.display_amount()
creditcard1.process_payment()
creditcard1.generate_payment()

upi1.display_amount()
upi1.process_payment()
upi1.generate_payment()

cash1.display_amount()
cash1.process_payment()
cash1.generate_payment()
'''
Amount is 10000
Processing Credit Card payment
Credit Card receipt generated
Amount is 7000
Processing UPI Card payment
UPI receipt generated
Amount is 3000
Processing Credit Card payment
Cash receipt generated
'''
