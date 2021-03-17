"""
Program: basicList
Author: Dylan Kennedy
Last date modified: 03/09/2021

TThe purpose of this program is to prompt the user for a number and append
it to the list.
"""

from re import match

def make_list(listSize):
    """
    Add numbers to a list of a given size.
    :params listSize
    :returns a list of nums.
    """
    nums = []
    for x in range(listSize):
        num = int(get_input("Please enter a whole number> ", "^\d+$",
                            "Please enter a valid number!"))
        nums.append(num)

    return nums

def get_input(prompt, pattern, error):
    """
    Check that the user's input matches a given pattern if not repeat.
    :params what to prompt the user, the regex pattern to match,
    and the error to print.
    :returns a validated string
    """
    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)

def main():
    
     print(make_list(1))
     print(make_list(2))
     print(make_list(3))

if __name__ == '__main__':
    main()
