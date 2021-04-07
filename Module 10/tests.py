from classDefinitions.employee import Employee
import unittest


class EmployeeTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(EmployeeTest, self).__init__(*args, **kwargs)
        self.testEmployee = Employee("Sasha", "Patel",
                                     "123 Main Street\nUrban, Iowa",
                                     "555-555-5555", "6-28-2019",
                                     40000, True)
        self.testEmployeeTwo = Employee("Steven", "Miller",
                                        "117 South Des Moines Iowa",
                                        "444-444-4444",
                                        "05-05-2005", 20.00)

    def test_str(self):
        """
        Tests that the Employee str() function behaviour matches the guide line
        outline here: https://www.tutorialspoint.com/str-vs-repr-in-python
        """
        expected = "Employee(Sasha, Patel, 123 Main Street\nUrban, Iowa, 555-555-5555, 6-28-2019, 40000, True)"
        actual = str(self.testEmployee)
        self.assertEqual(expected, actual)

    def test_repr(self):
        """
        Tests that the Employee repr() function behaviour matches the guide line
        outline here: https://www.tutorialspoint.com/str-vs-repr-in-python
        """
        expected = "'Employee(Sasha, Patel, 123 Main Street\nUrban, Iowa, 555-555-5555, 6-28-2019, 40000, True)'"
        actual = repr(self.testEmployee)
        self.assertEqual(expected, actual)

    def test_display_salried(self):
        """
        Test that display shows acurate info with salaried employees.
        """
        expected = "Sasha Patel\n123 Main Street\nUrban, Iowa\nSalaried employee: $40,000.00/year\nStart Date: 6-28-2019"
        actual = self.testEmployee.display()
        self.assertEqual(expected, actual)

    def test_display_hourly(self):
        """
        Test that display shows acurate info with hourly employees.
        """
        expected = "Steven Miller\n117 South Des Moines Iowa\nHourly employee: $20.00/hour\nStart Date: 05-05-2005"
        actual = self.testEmployeeTwo.display()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
