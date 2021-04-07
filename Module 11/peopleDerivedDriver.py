"""
Program: peopleDerived
Author: Dylan Kennedy
Last date modified: 04/06/2021

The purpose of this program is
to construct student objects and test that the respective functions work as intended.
"""

from peopleDerived import Student

if __name__== '__main__':
   my_student = Student(900111111, 'Song', 'River')
   print(my_student.display())
   my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
   print(my_student.display())
   my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
   print(my_student.display())
   del my_student
