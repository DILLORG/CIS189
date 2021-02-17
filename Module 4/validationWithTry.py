"""
Program: validationWithTryKennedy.py
Author: Dylan Kennedy
Last date modified: 02/09/2021

The purpose of this program is
to calculate the student's average score.
"""

NUM_TEST = 3

def average(scores):
    totalScore = 0.0

    for score in scores:
        totalScore += score

    return float(totalScore / NUM_TEST)


if __name__ == '__main__':
    scores = []
    count = 0

    while count < NUM_TEST:

        try:
            test = float(input(f"Please enter score for test {count +1}> "))

            if test < 0:
                raise ValueError
            else:
                scores.append(test)
                count+=1

        except ValueError:
            print("Invalid score!")


    averageScore = average(scores)

    print(f"The student's average score is {averageScore:.1f} ")
