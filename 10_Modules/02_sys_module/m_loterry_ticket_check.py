#!/usr/bin/python
"""
Purpose: Lottery Ticket Verifier
"""
import sys

winning_ticket = "123123kj12319088ad"

# hardcoded
# user_ticket = "ksagjdkjaskdjsak"

# # runtimr input
# user_ticket = input('Enter the user ticket:')

if len(sys.argv) != 2:
    print(f"{sys.argv =}")
    print("Please try your lotter ticket number also")
    print(f"{__file__} <YOUR LOTTERY TICKET NO>")
    print(f"{__file__} 123asdd123rdsr123dsa")
    sys.exit(1)


user_ticket = sys.argv[1]

if user_ticket == winning_ticket:
    print('You won the lottery')
else:
    print('Try Again!!!')

