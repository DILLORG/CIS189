"""
Program: couponCalculations
Author: Dylan Kennedy
Last date modified: 02/03/2021

The purpose of this program is
to calculate the customers total.
"""
from re import match

def decoder_ring(prompt, error, pattern):

    while True:
        var = input(prompt)

        if(match(pattern, var)):
            return var

        else:
            print(error)

SALES_TAX = 0.06
FIRST_TIER = 5.95
SECOND_TIER = 7.95
THIRD_TIER = 11.95
coupon = 0
discount = 0
subTotal = 0
total = 0
ship = 0

# Prompt user for subtotal.
subTotal = float(decoder_ring("Please enter the total of the purchase in dollars> $",
                              "Invalid input!", "^[1-9]\d*(\.\d{2})?$"))

# Only prompt for coupon and discount if total is greater than $10.00.
if(subTotal > 10.00):
    coupon = float(decoder_ring("Please enter either a $5.00 or $10.00 coupon> $",
                            "Invalid input", "(5|10)(\.00)?$"))

    discount = decoder_ring("Please enter a discount your options are 10%, 15%, 20%, or 30%> ",
                            "Invalid input", "(10|15|20|30)(\%)?$")
    discount = float(discount.replace('%', '')) / 100

    total = subTotal - coupon
    total = total - (total* discount)
    total = (SALES_TAX * total) + total

# Determine shipping cost.
if(total < 10.00):
    ship = FIRST_TIER
elif(total >= 10.00 and total < 30.00):
    ship = SECOND_TIER
elif(total >=30.00 and total < 50.00):
    ship = THIRD_TIER
else:
    ship = 0

# Calculate total.
total = total + ship
print(f"Your total is ${total:.2f}")
