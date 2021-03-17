"""
Program: driver
Author: Dylan Kennedy
Last date modified: 03/17/2021

Display results of module functions to console.
"""

from definitions.dictionaryOps import print_dict
from definitions.setOps import print_set
from definitions.greeting import friendly_greeting, print_author


def main():
    print_author()
    friendly_greeting()

    test_dict = {'A': 2, 'B': 3, 'C': 10}
    test_set = [1, 2, 4, 5]

    print_dict(test_dict)
    print_set(test_set)


if __name__ == '__main__':
    main()
