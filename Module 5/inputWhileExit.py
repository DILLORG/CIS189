"""
Program: inputWhileExit
Author: Dylan Kennedy
Last date modified: 02/17/2021

The purpose of this program is to promp the user to for a number between 1
and 100 and store that number in a list.
"""

from re import match


listOfNums = []
SENTINEL = "(Q|q|Quit|quit|QUIT)"

def print_nums():
    """
    Print all numbers stored in list.
    :params none
    :return list of numbers.
    """
    for num in listOfNums:
        print(num)


def decoder_ring(prompt, error, pattern, cancel):
    """
    Check that the users input matches a given pattern.
    If not print error and prompt again.
    :params prompt for user, error to print to console,  a regex pattern
    :return validated string.
    """
    while True:print(score_input('Test 1', 70))
    print(score_input('Test 2', -2))
    print(score_input('Test 3', 1000))
    print(score_input('Test 4', 'Dfdsfsd'))
        var = input(prompt)

        if(match(pattern, var)):
            return var

        elif(match(cancel, var)):
            print("Ok exiting...")
            print_nums()
            exit(0)

        else:
            print(error)

def main():
    value = ''
    while value != SENTINEL:

        # Prompt user for number in range 1-100. Repeat if not in range.
        value = int(decoder_ring(f"\nPlease enter a number between 1 and 100 or Q to quit> ",
                             "\nInvalid!", "([1-9]|[1-9][0-9]|100|)$",
                             f"{SENTINEL}"))
        print(f"Added {value} to list")
        # Add number to list.
        listOfNums.append(value)



if __name__ == '__main__':
    main()
