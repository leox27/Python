"""
#4. (Abstract Class with Multiple Abstract Methods)

Create an abstract class named Payment.
Requirements
Import ABC and abstractmethod from the abc module.
Create two abstract methods:
- pay()
- refund()

Create a child class named CreditCard.

Implement both abstract methods.
pay() should print:
"Payment made using Credit Card"
refund() should print:
"Amount refunded to Credit Card"

Create a CreditCard object.
Call both methods.
"""

from abc import ABC, abstractmethod

class Payment(ABC):
    
    @abstractmethod
    def pay(self):
        pass
    
    @abstractmethod
    def refund(self):
        pass

class CreditCard(Payment):
    
    def pay(self):
        print("Payment made using Credit Card")
        
    def refund(self):
        print("Amount refunded to Credit Card")
        
creditcard1 = CreditCard()

creditcard1.pay()
creditcard1.refund()
'''
Payment made using Credit Card
Amount refunded to Credit Card
'''
