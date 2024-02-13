#!/usr/bin/python3
"""
Purpose: Number Guessing Game

    break - To come out of any loop (for/while)
"""
LUCKY_NUMBER = 67
MAX_ATTEMPTS = 5

# # Method 1 - No limit on number of chances(attempt)
# given_number = int(input('Enter no. between 0 & 100:'))

# if given_number == LUCKY_NUMBER:
#     print('You guessed correctly!')
# elif given_number > LUCKY_NUMBER:  # 87 > 67
#     print('Reduce your guessing number')
# else:  # given_number < LUCKY_NUMBER
#     print('Increase your guessing number')


# Method 2 - To limit the number of attempts
# attempt = 0
# while attempt < MAX_ATTEMPTS:
#     attempt += 1
#     print(f'\n{attempt = }')

#     given_number = int(input('Enter no. between 0 & 100:'))
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')

#     if attempt == MAX_ATTEMPTS:
#         print(f'Sorry! YOu failed to guess in all {attempt} attempts'.upper())


# # Method 3 - while with else condition
# attempt = 0
# while attempt < MAX_ATTEMPTS:
#     attempt += 1
#     print(f'\n{attempt = }')

#     given_number = int(input('Enter no. between 0 & 100:'))
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')

# else: # attempt == MAX_ATTEMPTS:
#     print(f'Sorry! YOu failed to guess in all {attempt} attempts'.upper())


# # Method 4 - Check for user choice after each incorrect guess
# choice = 'Y'
# attempt = 0
# while choice == "Y":  # do-while loop 
#     attempt += 1
#     print(f'\n{attempt = }')

#     given_number = int(input('Enter no. between 0 & 100:'))
#     if given_number == LUCKY_NUMBER:
#         print('You guessed correctly!')
#         break
#     elif given_number > LUCKY_NUMBER:  # 87 > 67
#         print('Reduce your guessing number')
#     else:  # given_number < LUCKY_NUMBER
#         print('Increase your guessing number')
    
#     choice = input('Enter Y(or y) to continue .. ').upper()
# else:
#     print(f'Sorry! YOu failed to guess in all {attempt} attempts'.upper())


# Method 5 - Giving Infinite Attempts; but tracking attempts
attempt = 0
while True:  # do-while loop 
    attempt += 1
    print(f'\n{attempt = }')

    given_number = int(input('Enter no. between 0 & 100:'))
    if given_number == LUCKY_NUMBER:
        print('You guessed correctly!')
        break
    elif given_number > LUCKY_NUMBER:  # 87 > 67
        print('Reduce your guessing number')
    else:  # given_number < LUCKY_NUMBER
        print('Increase your guessing number')
# else:  # CODE IS NOT REACHABLE
#     print("It will never reach here, as loop breaks to exit")


"""
    Assignment
    ------------------------
    attempts        points
    -----------------------
    1-3             100
    4-9              60
    10-16            20
    17-25             5
    26-               0
"""