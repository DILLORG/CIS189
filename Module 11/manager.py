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

class Employee:
   def __init__(self, id, salary, startDate):
      """
      Constructs all employee objects
      :params firstName, lastName, address, phoneNumber, startDate, salary
               salaried
      :returns Employee object
      """
      
      self.id = id
      self.salary = salary
      self.startDate = startDate
   
   def change_salary(self, value):
      """Determines if the given value is at least equal to the employee current pay rate if not raise ValueError
      :params value
      :return none"""
      if self.salary <= value:
         self.salary = value
      else:
         raise ValueError(f"Attempted to give employee less than they currently make {self.salary} > {value}")
   
   def display(self):
      """Return formated string representing employee
      :params none
      :return formated string"""
      return f"Employee ID: {self.id}\nSalary: ${self.salary:,.2f}\nStart Date: {self.startDate}"


class Manager(Person, Employee):
   def __init__(self, lname, fname, id, salary, startDate, department, directReports=[], address=''):
      """Constructs all manager objects raisese ValueError if the directReports is not a valid list."""
      if type(directReports) is list:
         
         Person.__init__(self, lname, fname, address)
         Employee.__init__(self, id, salary, startDate)
         self.department = department
         self.directReports = directReports
      
      else:
         raise ValueError(f"{type(directReports)} is invalid for option directReports")
   
   def display_reports(self):
      """
      Iterate over subordinates and print them to the console
      :params none
      :returns none
      """
      print(f"{self.last_name}, {self.first_name} has the following subordinates:")
      for employee in self.directReports:
         print(employee.display())
   
   def display(self):
      """Return formated string representing mananger
      :params none
      :return formated string"""
      return f"Name: {self.first_name}, {self.last_name}\nSalary: ${self.salary:,.2f}\nStartDate:{self.startDate}\nDepartment:{self.department}"
