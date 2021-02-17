"""
Program: inputWhile
Author: Dylan Kennedy
Last date modified: 02/17/2021

The purpose of this program is
to generate random floats and then print them to the
console using a for loop.
"""

from re import match

def decoder_ring(prompt, error, pattern):
    """
    Check that the users input matches a given pattern.
    If not print error and prompt again.
    :params prompt for user, error to print to console,  a regex pattern
    :return validated string.
    """
    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)


SENTINEL = 'Q'
listOfNums = []
value = ''

while value != SENTINEL:

    # Prompt user for number in range 1-100. Repeat if not in range.
    value = decoder_ring(f"\nPlease enter a number between 1 and 100 or {SENTINEL} to quit> ",
                         "\nInvalid!", f"([1-9]|[1-9][0-9]|100|{SENTINEL})$")
    # Add number to list.
    try:
        print(f"\nAdding {value} to list")
        listOfNums.append(int(value))

    # User wishes to quit.
    except ValueError:
        print("Ok exiting...")


# Print all valid numbers.
for num in listOfNums:
    print(num)
