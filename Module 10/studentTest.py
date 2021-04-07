"""
Program: studentTest
Author: Dylan Kennedy
Last date modified: 02/17/2021

The purpose of this program is
to construct student objects and test that the respective functions work as intended.
"""

from student import Student
import unittest

class StudentTest(unittest.TestCase):
   def setUp(self):
      self.student = Student("Smith", "Steven", "CIS")
   
   def tearDown(self):
      del self.student
   
   def test_object_creates_required_attributes(self):
      self.assertEqual("Smith", self.student.last_name)
      self.assertEqual("Steven", self.student.first_name)
      self.assertEqual("CIS", self.student.major)
   
   def test_object_creates_all_attributes(self):
      student = Student("Smith", "Steven", "CIS", 4.0)
      self.assertEqual("Smith", student.last_name)
      self.assertEqual("Steven", student.first_name)
      self.assertEqual("CIS", student.major)
      self.assertEqual(4.0, student.gpa)
   
   def test_student_str(self):
      expected = "Smith, Steven has major CIS with gpa: 0.0"
      actual = str(self.student)
      self.assertEqual(expected, actual)
   
   def test_object_error_last_name(self):
      with self.assertRaises(ValueError):
         student = Student("123", "Steven", "CIS")
   
   def test_object_error_first_name(self):
      with self.assertRaises(ValueError):
         student = Student("Smith", "567", "CIS")
   
   def test_object_error_major(self):
      with self.assertRaises(ValueError):
         student = Student("Smith", "Steven", "325")
   
   def test_object_error_gpa_range(self):
      with self.assertRaises(ValueError):
         student = Student("Smith", "Steven", "CIS", 5.6)
   
   def test_object_error_gpa_type(self):
      with self.assertRaises(ValueError):
         student = Student("Smith", "Steven", "CIS", 5)
         

if __name__ == '__main__':
   studentOne = Student("Kennedy", "Dylan", "CIS", 4.0)
   studentTwo = Student("Jenkins", "Shelly", "Nursing", 4.0)
   print(str(studentOne))
   print(str(studentTwo))
   print("Running Test Now")
   
   unittest.main()
   
   
      
