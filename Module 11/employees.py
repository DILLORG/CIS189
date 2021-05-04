class Employee:
   def __init__(self, fname, lname, address, phoneNumber):
      """
      Constructs all employee objects
      :params firstName, lastName, address, phoneNumber, startDate, salary
               salaried
      :returns Employee object
      """
      self.firstName = fname
      self.lastName = lname
      self.address = address
      self.phoneNumber = phoneNumber

   def __str__(self):
      return f"Employee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber})"

  def __repr__(self):
     return f"'Employee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber})'"


class SalariedEmployee(Employee):
   def __init__(self, fname, lname, address, phoneNumber, startDate, salary):
      Employee.__init__(self, fname, lname, address, phoneNumber)
      self.startDate = startDate
      self.salary = salary

   def give_raise(self, value):
      """
      Determines if the given value is at least equal to their salary
      if not raise  ValueError
      :params value
      :returns none
      """
      if self.salary <= value:
         self.salary = value

      else:
         raise ValueError(f"Attempted to give {self.firstName} {self.lastName} less than they make {value} < {self.salary}")

   def display(self):
        """
        :paramas none
        :returns formated employee info.
        """
        return f"{self.firstName} {self.lastName}\n{self.address}\nSalaried: ${self.salary:,.2f}/year\nStart Date: {self.startDate}"

   def __str__(self):
      return f"SalariedEmployee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber}, {self.startDate}, {self.salary})"

   def __repr__(self):
      return f"'SalariedEmployee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber}, {self.startDate}, {self.salary})'"


class HourlyEmployee(Employee):
   def __init__(self, fname, lname, address, phoneNumber, startDate, hourlyPay):
      Employee.__init__(self, fname, lname, address, phoneNumber)
      self.startDate = startDate
      self.hourlyPay = hourlyPay

   def give_raise(self, value):
      """Determines if the given value is at least equal to their current pay if not raise a value error.
      :params value
      :returns none"""
      if self.hourlyPay <= value:
         self.hourlyPay = value
      else:
         raise ValueError(f"Attempted to give {self.firstName} {self.lastName} less than they currently make {value} < {self.hourlyPay}")

   def display(self):
      """
      :paramas none
      :returns formated employee info.
      """

      return f"{self.firstName} {self.lastName}\n{self.address}\nHourly: ${self.hourlyPay:,.2f}/hour\nStart Date: {self.startDate}"

   def __str__(self):
      return f"SalariedEmployee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber}, {self.startDate}, {self.hourlyPay})"

   def __repr__(self):
      return f"'SalariedEmployee({self.firstName}, {self.lastName}, {self.address}, {self.phoneNumber}, {self.startDate}, {self.hourlyPay})'"
