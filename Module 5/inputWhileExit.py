"""
Program: inputWhileExit
Author: Dylan Kennedy
Last date modified: 02/17/2021

The purpose of this program is
to generate random floats and then print them to the
console using a for loop.
"""

from re import match

def decoder_ring(prompt, error, pattern, cancel):
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

        elif(cancel, var):
            print("Ok exiting...")
            exit(0)

        else:
            print(error)


SENTINEL = 'Q'
listOfNums = []
value = ''

while value != SENTINEL:

    # Prompt user for number in range 1-100. Repeat if not in range.
    value = int(decoder_ring(f"\nPlease enter a number between 1 and 100 or {SENTINEL} to quit> ",
                             "\nInvalid!", "([1-9]|[1-9][0-9]|100|)$",
                             f"{SENTINEL}"))
    # Add number to list.
    listOfNums.append(value)


# Print all valid numbers.
for num in listOfNums:
    print(num)
