"""
Program: driver
Author: Dylan Kennedy
Last date modified: 04/06/2021

The purpose of this program is
to construct student objects and test that the respective functions work as intended.
"""

from people import Student, Person

"""
 In this assignment, you will create a class with a data member of the type of a class you defined.
Student is a Person with a major, a start date and a gpa. Use the Person class defined above.
Define a Student class with methods change_major(), update_gpa() and display() that returns a string.
Include a driver that

    Creates a student object (select a meaningful name) with your name, major, start date and 4.0 gpa
    Displays the student
    Changes the major to 'Being Awesome!'
    Updates the gpa to 3.0
    Displays the student
    Performs garbage collection
Your directions seemed to be split between creating a derived class and having a data meber of type person.
"""

if __name__ == '__main__':
   me = Person("Kennedy", "Dylan", "123 Main Street")
 
   studentOne = Student(me, "Computer Science", "Oct 6 2020", 4.0)

   studentOne.change_major("Being Awesome")
   studentOne.update_gpa(3.0)

   print(studentOne.display())
   del studentOne
