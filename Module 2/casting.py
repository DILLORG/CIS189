"""
Program: casting
Author: Dylan Kennedy
Last date modified: 01/26/2021

The purpose of this program is
to accept integer as input and out put them
"""

MAX_NUMS = 5
count = 0

while count < MAX_NUMS:

    # Attempt to cast user input to int.
    try:
        userInput = int(input(f"\nPlease enter the number {count + 1}> "))
        print(f"I asked for: {count + 1}\t You gave me: {userInput}")
        count += 1

    # User passed value that is not an integer
    except ValueError:
        print("I only like whole numbers!")
