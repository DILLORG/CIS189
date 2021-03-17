"""
Program: averageScores
Author: Dylan Kennedy
Last date modified: 02/02/2021

The purpose of this program is
to calculate the users average score.
"""

from re import match


def decoder_ring(prompt, error, pattern):

    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)


totalScore = 0

# Validate input based upon regular expressions
firstName = decoder_ring("Please enter student's first name> ",
                         "Please enter a valid first name!",
                         "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")

lastName = decoder_ring("Please enter student's last name> ",
                        "Please enter a valid last name",
                        "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")

age = int(decoder_ring("Student's age> ",
                       "Please enter a valid age!", "^\d+$"))

NUM_TEST_SCORES = 5

# for x in the range of scores.
for x in range(NUM_TEST_SCORES):
    score = int(decoder_ring(f"Please enter the score for test {x + 1}> ",
                             "Pleae enter valid score! \n", "^\d+$"))

    # add score to totalScore
    totalScore += score

# Calulate average.
average = totalScore/NUM_TEST_SCORES

# Print student's info
print(f"{lastName}, {firstName} age: {age} average grade: {average:.2f}")
