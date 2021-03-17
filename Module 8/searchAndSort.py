"""
Program: searchAndSort
Author: Dylan Kennedy
Last date modified: 03/16/2021

The purpose of this program is to search an array for a value and sort said
array.
"""
import array as ar


def sort_array(container):
    """
    Sorts a given list. I returned the sorted list so that the new order can be
    persisted if desired.
    :params a given container
    :returns a sorted list
    """
    return sorted(container)


def search_array(container, value):
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
        return f"{value} is not in array"


def main():
    container = ar.array('I', [10, 5, 7, 8, 9])
    print(f"Unsorted container: {container.tolist()}")
    print(search_array(container, 5))
    print(f"Sorted container: {sort_array(container)}")


if __name__ == '__main__':
    main()
