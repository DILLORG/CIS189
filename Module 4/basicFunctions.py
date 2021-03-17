"""
Program: basicFunctions
Author: Dylan Kennedy
Last date modified: 02/09/2021

The purpose of this program is
to ask the user to input their name hours work and pay rate.
"""
from re import match


def decoder_ring(prompt, error, pattern):
    """
    Check that the user's input matches a given pattern if not repeat.
    """

    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)


def hourly_employee_input():
    """
    Prompt the user to enter their name hours worked
    and pay rate to determine gross pay
    :params none
    :returns string.
    """

    name = decoder_ring("Please enter your name> ",
                        "Name invalid!",
                        "^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$")

    hoursWorked = int(decoder_ring("Please enter the hours you have worked this week> ",
                                   "Please enter a number in the range 0-80!",
                                   "([1-9]|[1-7][0-9]|80)$"))

    payRate = float(decoder_ring("Please enter your hourly pay rate> $ ",
                                 "Please enter a valid pay rate!",
                                 "^[1-9]\d*(\.\d{2})?$"))

    grossPay = weekly_pay(payRate, hoursWorked)

    return f""" \nName: {name}\nHours Worked: {hoursWorked}
                \nPay Rate: ${payRate:.2f} \nGross Pay: ${grossPay:.2f}"""


def weekly_pay(payRate, hoursWorked):
    """Calculate the weekly pay rate.
    :param payRate, hoursWorked
    :returns what the employee makes in a week.
    """
    return payRate * hoursWorked


if __name__ == '__main__':
    result = hourly_employee_input()
    print(result)
