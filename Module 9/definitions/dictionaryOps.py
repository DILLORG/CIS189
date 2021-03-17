def print_dict(container):
    """
    Print the key and value for every item in the container.
    :params container a dictionary.
    :return each key and value to the console.
    """

    for key, value in container.items():
        print(f"Key:{key} Value:{value}")
