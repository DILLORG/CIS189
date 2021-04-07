from employees import SalariedEmployee, HourlyEmployee

if __name__ == '__main__':
   
   employee = SalariedEmployee('Dylan', 'Kennedy', '123 Main Street', '555-555-5555', '04-06-2021', 40000)
   employee.give_raise(45000)
   print(employee.display())
   del employee
   
   employee = HourlyEmployee('Dylan', 'Kennedy', '123 Main Street', '555-555-5555', '04-06-2021', 10.00)
   employee.give_raise(12.00)
   print(employee.display())
   employee.give_raise(10.00)
   del employee
   
   
