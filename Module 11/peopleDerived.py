class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):   
        self._last_name = lname
        self._first_name = fname
        self._address = addy


    def display(self):
        return f"{self._last_name}, {self._first_name}:{self._address}"

class Student(Person):
   def __init__(self, studentId, lname, fname, addy='', major='Computer Science', gpa=0.0):
      Person.__init__(self, lname, fname, addy)
      self._studentId = studentId
      self._major = major
      self._gpa = gpa
   
   def display(self):
      return f"{self._last_name}, {self._first_name}:({self._studentId}) {self._major} gpa {self._gpa} "
      
