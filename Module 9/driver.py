"""
Program: driver
Author: Dylan Kennedy
Last date modified: 03/17/2021

Display results of module functions to console.
"""

from myDefinitions import print_author, friendly_greeting
from myDefinitions import print_dict, print_set


def main():
    print_author()
    friendly_greeting()

    test_dict = {'A': 2, 'B': 3, 'C': 10}
    test_set = [1, 2, 4, 5]

    print_dict(test_dict)
    print_set(test_set)


if __name__ == '__main__':
    main()
