from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using Credit Card")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using UPI payment")

class NetBankingPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount:.2f} using Netbanking payment")

# Different objects with the same interface
payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

# Runtime polymorphism:
# The same pay() call behaves differently for each object.
print("Processing a Payment")
for p in (payments):
    p.pay(10000)