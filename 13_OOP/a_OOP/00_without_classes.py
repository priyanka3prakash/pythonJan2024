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

def deposit(customer_bal, amount):
    customer_bal = customer_bal + amount 
    return customer_bal

def withdraw(customer_bal, amount):
    customer_bal = customer_bal - amount 
    return customer_bal

if __name__ == '__main__':
    customer1_balance = 0
    print(f"Customer1     - Initial balance:", customer1_balance)
    
    customer1_balance = deposit(customer1_balance, 1000)
    print(f"After Deposit - 1000, balance  :", customer1_balance)

    customer1_balance = withdraw(customer1_balance, 200)
    print(f"After withdraw - 200, balance  :", customer1_balance)
    print()


    customer2_balance = 0
    print(f"Customer2     - Initial balance:", customer2_balance)
    
    customer2_balance = deposit(customer2_balance, 3500)
    print(f"After Deposit - 3500, balance  :", customer2_balance)

    customer2_balance = withdraw(customer2_balance, 550)
    print(f"After withdraw - 550, balance  :", customer2_balance)
 