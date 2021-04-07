"""
Program: managerDriver
Author: Dylan Kennedy
Last date modified: 04/06/2021

The purpose of this program is
to construct manager objects and test that the respective functions work as intended.
"""


from manager import Employee,  Manager
from datetime import date
if __name__ == '__main__':
   employees = []
   
   for x in range(10):
      # Genrate Employees
      employees.append(Employee(7.25 * 599, x * 1000, date.today()))
   boss = Manager('Kennedy', 'Dylan', 5954543, 40000,  date.today(), 'Manager', directReports=employees)
   boss.display_reports()
   
   boss.change_salary(42000)
   
   # Manager's Display method called.
   print(boss.display())
