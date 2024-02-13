#!/usr/bin/python3
"""
Purpose: Progress Status Bar Implementation

    Escape Sequences
        \t - tab space
        \n - new line
        \r - rare feed
"""
print("Udhay Prakash")
print("Udhay\tPrakash")
print("Udhay\nPrakash")
print()

print("Udhay\bPrakash")
print("Prakash\bUdhay")
print()

print("Udhay\rPrakash")  # Prakash
print("Prakash\rUdhay")  # Udhaysh
print()


print("1234567890\rDOG")    # DOG4567890
print("abcdef\r123")        # 123def


data_set = range(-100, 10_00_000)
data_set_length = len(data_set)


# for num in data_set:
#     print(num)


# for loop_index, num in enumerate(data_set):
#     print(loop_index, num)

for loop_index, _ in enumerate(data_set):
    # print(loop_index, loop_index / data_set_length)
    percent_completed = (loop_index / data_set_length) * 100
    percent_completed = round(percent_completed, 2)

    # print(percent_completed, end="\r")
    # print(f"{percent_completed:5} completed", end="\r")
    print(f"\r{percent_completed:5} completed", end="")



"""
Assignment: Progress bar implementation
    [          ]   3
    [*         ]  10
    [**        ]  20
    [***       ]  30
    [****      ]  40
    [*****     ]  50
    [******    ]  60
    [*******   ]  70
    [********  ]  80
    [********* ]  90
    [**********] 100
"""