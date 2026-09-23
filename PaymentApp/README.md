Polymorphism + Abstraction

Build a payment-processing example with an abstract Payment class containing a pay() method. Implement CreditCardPayment, UPIPayment, and NetBankingPayment. Demonstrate runtime polymorphism by calling the same method on different payment objects.

Sample Input:
payments = [
    CreditCardPayment(),
    UPIPayment(),
    NetBankingPayment()
]

Sample Output:
Processing a Payment
Paid ₹10000.00 using Credit Card
Paid ₹10000.00 using UPI payment
Paid ₹10000.00 using Netbanking payment