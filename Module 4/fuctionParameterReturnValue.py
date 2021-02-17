"""
Program: functionParameterReturnValue
Author: Dylan Kennedy
Last date modified: 02/09/2021

Prompts the user for a string and the amount of times they would like to see
the string repeated.
"""
def decoder_ring(prompt, error, pattern):
    """
    Check that the user's input matches a given pattern if not repeat.
    :params prompt, error, pattern
    :returns validated string.
    """

    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)

def multipy_string(message, numTimes):
    """
    Return the message repeated the amount of times specified.
    :params message, numTimes
    :returns the message repeated
    """

    return message * numTimes

def main():
    message = input("\nPlease enter the desired message> ")
    try:
        numTimes = int(input("\nPlease enter the amount of times to repeat> "))
        print(multipy_string(message, numTimes))
    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    assert (multipy_string("Python", 4) == "PythonPythonPythonPython")
    main()
