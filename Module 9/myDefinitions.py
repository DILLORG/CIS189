def print_set(container):
    """
    Prints all the values in a given set.
    :params container a set.
    :returns the value of each item in the set to the console.
    """
    for item in container:
        print(item)


def print_dict(container):
    """
    Print the key and value for every item in the container.
    :params container a dictionary.
    :return each key and value to the console.
    """

    for key, value in container.items():
        print(f"Key:{key} Value:{value}")


def friendly_greeting():
    """
    Prints a friendly greeting to the console.
    :params none
    :returns none
    """
    print("Hello there!")


def print_author():
    """
    Prints the authors name.
    :params none
    :returns none
    """
    print("author: Dylan Kennedy")
