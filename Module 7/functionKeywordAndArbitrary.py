
"""
Program: functionKeywordAndArbitrary
Author: Dylan Kennedy
Last date modified: 03/09/2021

The purpose of this program is to calculate the student's average score given
a set of arbitrary arguments the students info is stored in keywords.
"""

def average_scores(*args, **kwargs):
    """
    Calculate students average with arbitrary Arguments.
    :params args the student's scores. kwargs student's name gpa and course
    :returns formatted string with the students info
    and the average of their scores.
    """
    # Use *args for average calculation
    total = 0
    for arg in args:
        total += arg

    average = total / len(args)

    # return
    return f"Result: name = {kwargs['name']} gpa = {kwargs['gpa']} course = {kwargs['course']} with current average of {average}"

def main():
    print(average_scores(4, 3, 2, 4, name='M', course='Python', gpa=3.2))
    print(average_scores(300, 100, 20, name='Steven', course='C++', gpa=4.0))
    print(average_scores(305, name='Gary', course='History', gpa=4.0))

if __name__ == '__main__':
    main()
