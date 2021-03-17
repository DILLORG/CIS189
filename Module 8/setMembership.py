"""
Program: setMembership
Author: Dylan Kennedy
Last date modified: 03/16/2021

The purpose of this program is to determine whether or not an item is in a
given set.
"""


def in_set(container, value):
    """
    Determine if a given value is in a given set.
    :params value, container
    :return a string of declaring if the value is in the set.
    """

    """
    Your instructions are unclear. You say to return a bool
    but ask that the function state if the element is in the set.
    Are the messages to be printed in main if the function returns true or is
    this function to return a message?
    """
    if value in container:
        return f"The value '{value}' is in the set {container}"

    else:
        return f"The value '{value}' is not in the set {container}"


def main():
    """
    Declare a set and pass it to in_set to determine if it is in the set.
    print results to console.
    :params none.
    :returns result of call to in_set.
    """
    container = {'banana', 'apple', 'cherry'}
    print(in_set(container, 'apple'))
    print(in_set(container, 5))


if __name__ == '__main__':
    main()
