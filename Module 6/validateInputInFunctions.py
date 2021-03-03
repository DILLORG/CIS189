"""
Program: validateInputInFunctions
Author: Dylan Kennedy
Last date modified: 03/02/2021

The purpose of this program is to validate that the test score is
in between the range 0 and 100 and is an integer.
"""

def score_input(testName, testScore=-1):
    """
    Determine if a given score is withing the range 0-100 if not return an
    error.
    :params testName, testScore
    :returns string representing result.
    """

    testScore = int(testScore)

    if(0 <= testScore <=100):
        return f"Score for {testName} is {testScore}"

    else:
        return "Invalid test score!"



def main():
    """
    Test  that the function handles all posible scenarios.
    :params none
    :returns none
    """

    try:
        print(score_input('Test 1', 70))
        print(score_input('Test 2', -2))
        print(score_input('Test 3', 101))
        print(score_input('Test 4', 'Dfdsfsd'))

    except ValueError:
        print("ValueError encounterd")

if __name__ == '__main__':
    main()
