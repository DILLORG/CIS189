"""
Program: sortAndSearch
Author: Dylan Kennedy
Last date modified: 03/09/2021

The purpose of this program is to prompt the user for a number and append
it to the list. It then prompts the user for a number to search the list for
it then sorts the list in numeric order.
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


def sort_list(container):
    """
    Sorts a given list. I returned the sorted list so that the new order can be
    persisted if desired.
    :params a given container
    :returns a sorted list
    """
    container.sort()
    return container


def search_list(value, container):
    """
    Finds the index where the value is held
    Returns a string so that we can input more info to the user.
    The index function returns a integer value.
    :params value to search for, container to search
    : returns a string showing the location of the given value.
    """

    try:
        foundAt = container.index(value)
        return f"Found {value} at index {foundAt}"

    except ValueError:
        return f"{value} is not in list"


def main():

    listOfNums = make_list(5)
    value = int(get_input("Please enter the value to search for> ",
                          "^\d+$", "The value must be a number"))

    print(search_list(value, listOfNums))
    print(f"Sorted list: {sort_list(listOfNums)}")


if __name__ == '__main__':
    main()
