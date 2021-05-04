"""Program: driver
Author: Dylan Kennedy
Last date modified: 04/27/2021

The purpose of this program is prompt the parent to enter the age of their
child in years and convert that into months.
"""

from re import match


def convert_to_months(years):
    MIN_AGE = 1
    MAX_AGE = 5
    pattern = f"[{MIN_AGE}-{MAX_AGE}]$"

    if match(pattern, years):
        months = int(years) * 12
        return months

    raise ValueError(f"Campers must be {MIN_AGE}-{MAX_AGE} years old")


if __name__ == '__main__':
    age_in_years = '3'
    age_in_months = convert_to_months(age_in_years)

    print(f"{age_in_years} years is {age_in_months} months old")

    age_in_years = input("How old is your child in years> ")
    age_in_months = convert_to_months(age_in_years)

    print(f"{age_in_years} years is {age_in_months} months old")
