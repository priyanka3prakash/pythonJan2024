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
def create_account():
    return {'balance': 0}


def deposit(account, amount):
    account['balance'] += amount

def withdraw(account, amount):
    account['balance'] -= amount

if __name__ == '__main__':
    customer1 = create_account()
    print(f"Customer1     - Initial balance:", customer1['balance'])
    
    deposit(customer1, 1000)
    print(f"After Deposit - 1000, balance  :", customer1['balance'])

    withdraw(customer1, 200)
    print(f"After withdraw - 200, balance  :", customer1['balance'])
    print()


    customer2 = create_account()
    print(f"Customer2     - Initial balance:", customer2['balance'])
    
    deposit(customer2, 3500)
    print(f"After Deposit - 3500, balance  :",  customer2['balance'])

    withdraw(customer2, 550)
    print(f"After withdraw - 550, balance  :",  customer2['balance'])
 