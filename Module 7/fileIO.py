"""
Program: fileIO
Author: Dylan Kennedy
Last date modified: 03/09/2021

The purpose of this program is to prompt the user for their info and append it
to a file. Then read from the file and print to the console.
"""
from re import match
import os
FILE = os.path.join(os.path.dirname(__file__), 'student_info.txt')
NUM_STUDENTS = 4

def decoder_ring(prompt, error, pattern):
    """
    Check that the user's input matches a given pattern if not repeat.
    :params prompt, error, regex pattern
    :returns validated string.
    """

    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)

def write_to_file(studenInfo):
    """
    Write student info to the file.
    Using a option so that if the file exist it is not overwritten
    :params tuple containing the student info.
    :returns None
    """
    with open(FILE, 'a') as inFile:
        inFile.write(f"Name: {studenInfo[0]} Scores: {studenInfo[1]}\n")

def read_from_file():
    """
    Read each students information from file and prints it to the console.
    :params none
    :returns none.
    """
    with open(FILE, 'r') as inFile:
        for line in inFile:
            print(line)

def get_student_info():
    """
    Prompt user for their name and the number of test scores they had
    Call write to file to store them.
    :params none.
    :returns none.
    """
    tests = []
    name = decoder_ring("Please enter your name> ",
                        "Name invalid!",
                        "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")

    numTest = int(decoder_ring("How many scores do you have?> ",
                               "Please enter a valid age!", "^\d+$"))

    for x in range(numTest):
        score = int(decoder_ring(f"Please enter the score for test {x + 1}> ",
                             "Pleae enter valid score! \n", "^\d+$"))
        tests.append(score)

    studenInfo = name, tests
    write_to_file(studenInfo)

def main():
    for x in range(NUM_STUDENTS):
        get_student_info()

    read_from_file()

if __name__ == '__main__':
    main()
