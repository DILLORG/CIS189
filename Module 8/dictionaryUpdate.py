"""
Program: dictionaryUpdate
Author: Dylan Kennedy
Last date modified: 03/16/2021

The purpose of this program is to the average of the users scores.
It stores the scores in a dict.
"""

from re import match


def decoder_ring(prompt, error, pattern):
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


def get_test_scores():
    """
    Prompt user to enter their test scores and store them in a dict.
    :params none.
    :returns the dict of scores.
    """
    scoresDict = dict()
    numScores = int(decoder_ring("Please enter the number of test scores> ",
                                 "Please enter a valid number", "^\d+$"))
    for x in range(numScores):
        score = float(decoder_ring(f"Please enter your score for test {x +1}> ",
                                   "Your score must be in the range 0-100",
                                   "([0-9]|[1-9][0-9])(\.\d+)?$|100$"))
        scoresDict[x+1] = score
    return scoresDict


def average_scores(scores):
    """
    Return the average of the users scores.
    :params a dict of scores.
    :returns the average of the scores.
    """
    total = 0
    for score in scores.values():
        total += score

    return total / len(scores)


def main():
    scores = get_test_scores()
    average = average_scores(scores)
    print(scores)
    print(f"Your average is {average}")


if __name__ == '__main__':
    main()
