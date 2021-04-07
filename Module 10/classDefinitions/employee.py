class Employee:
    """Employee Class"""
    def __init__(self, firstName, lastName, address, phoneNumber, startDate,
                 salary,  salaried=False):
        """
        Constructs all employee objects
        :params firstName, lastName, address, phoneNumber, startDate, salary
                salaried
        :returns Employee object
        """
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__phoneNumber = phoneNumber
        self.__startDate = startDate
        self.__salary = salary
        self.__salaried = salaried

    @property
    def firstName(self):
        """
        :params none
        :returns firstname
        """
        return self.__firstName

    @firstName.setter
    def firstName(self, value):
        """
        :params new value of firstName
        :returns none
        """
        self.__firstName = value

    @property
    def lastName(self):
        """
        :params none
        :returns lastName
        """
        return self.__lastName

    @lastName.setter
    def lastName(self, value):
        """
        :params new value of lastname
        :returns none.
        """
        self.__lastName = value

    @property
    def address(self):
        """
        :params none
        :returns address
        """
        return self.__address

    @address.setter
    def address(self, value):
        """
        :params new value of address
        :returns none
        """
        self.__address = value

    @property
    def phoneNumber(self):
        """
        :params none
        :returns the value of phonenumber
        """
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, value):
        """
        :params new value of phoneNumber
        :returns none.
        """
        self.__phoneNumber = value

    @property
    def startDate(self):
        """
        :params none
        :returns startDate.
        """
        return self.__startDate

    @startDate.setter
    def startDate(self, value):
        """
        :params new value of startDate
        :returns none.
        """
        self.__startDate = value

    @property
    def salary(self):
        """
        :params none
        :returns salary.
        """
        return self.__salary

    @salary.setter
    def salary(self, value):
        """
        :params new value of salary
        :returns none.
        """
        self.__salary = value

    @property
    def salaried(self):
        """
        :params none
        :returns salaried.
        """
        return self.__salaried

    @salaried.setter
    def salaried(self, value):
        """
        :params new value of salaried
        :returns none.
        """
        self.__salaried = value

    def display(self):
        """
        :paramas none
        :returns formated employee info.
        """
        employeeType = "Hourly employee"
        payRate = "hour"
        if self.__salaried:
            employeeType = "Salaried employee"
            payRate = "year"

        return f"{self.__firstName} {self.__lastName}\n{self.__address}\n{employeeType}: ${self.__salary:,.2f}/{payRate}\nStart Date: {self.__startDate}"

    def __str__(self):
        """
        :params none
        :returns informal string.
        """
        return f"Employee({self.__firstName}, {self.__lastName}, {self.__address}, {self.__phoneNumber}, {self.__startDate}, {self.__salary}, {self.__salaried})"

    def __repr__(self):
        """
        :params none
        :returns formal  string.
        """
        return f"'Employee({self.__firstName}, {self.__lastName}, {self.__address}, {self.__phoneNumber}, {self.__startDate}, {self.__salary}, {self.__salaried})'"
