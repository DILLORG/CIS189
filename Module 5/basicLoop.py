"""
Program: basicLoop.py
Author: Dylan Kennedy
Last date modified: 02/17/2021

The purpose of this program is
to generate random floats and then print them to the
console using a for loop.
"""

import random

randomNums = []

# Generate 100 random floats between 0 and 100
for x in range(100):
    randomNums.append(round(random.uniform(0, 100), 2))


# Print numbers
print("\nAll Numers in list")
for num in randomNums:
    print(num)

# Sort list decending
randomNums.sort(reverse=True)

print("\nNumbers sorted in decending order and between 33 and 99")

for num in randomNums:

    # Number is odd and between the range of 33 and 99.
    if (num % 2) != 0 and 33 <= num <=99  :
        print(num)
