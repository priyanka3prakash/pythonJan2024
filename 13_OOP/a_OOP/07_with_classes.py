"""
Purpose: without OOPS, solving a problem

    Problem - To create a saving bank with facilitates transactions

        customer 1
                                                Balance
            Account creation                        0
            Transaction 1 - deposit  1000        1000
            Transaction 2 - withdraw  200         800

        Customer 2
                                                Balance
            Account creation                        0
            Transaction 1 - deposit  3500        3500
            Transaction 2 - withdraw  550        2950

"""

class Account:
    def __init__(self, name):
        self.balance = 0
        self.account_holder = name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_balance(self):
        return f"Account Balance for {self.account_holder} is {self.balance}"



if __name__ == '__main__':
    customer1 = Account('sudha')
    # print(f"Customer1     - Initial balance:", customer1.balance)
    print(f"Initial balance:", customer1.display_balance())
    
    customer1.deposit(1000)
    print(f"After Deposit - 1000, balance  :", customer1.display_balance())

    customer1.withdraw(200)
    print(f"After withdraw - 200, balance  :", customer1.display_balance())#
    print()

    mohana = Account('Mohana')
    print(f"Initial balance:", mohana.display_balance())
    
    mohana.deposit(1000)
    print(f"After Deposit - 1000, balance  :", mohana.display_balance())

    mohana.withdraw(200)
    print(f"After withdraw - 200, balance  :", mohana.display_balance())#
    print()


# Assignment: create a PersonLoan and savings Account