class Person:
    """Person class using class Address, Class Composition"""
    def __init__(self, lname, fname, address=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = address

    def display(self):
        return f"{self.last_name}, {self.first_name}\n{self.address}"

class Student:
   """Student Class"""
   def __init__(self, person, major, startDate, gpa):
      """Construct all student objects"""
      self.person = person
      self.major = major
      self.startDate = startDate
      self.gpa = gpa

   def change_major(self, value):
      """Change major change the value of the students major 
      :params value
      :returns none.
      """
      self.major = value

   def update_gpa(self, value):
      """
      Update gpa 
      Changes the value of gpa 
      :params value
      :returns none
      """
      self.gpa = value

   def display(self):
      
      """
      Display the student's info
      :params none
      :return none
      """
      return f"{self.person.display()} \nThey started {self.startDate}\nthey have a major of {self.major} and a gpa of {self.gpa}"

class Employee(Person):
   def __init__(self, lname, fname, addy='')
