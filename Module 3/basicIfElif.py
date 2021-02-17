"""
Program: basicIfElif
Author: Dylan Kennedy
Last date modified: 02/02/2021

The purpose of this program is
to ask the user for their budget
and determine what subscription level is best for them.
"""
PLATINUM_TIER = 60.00
GOLD_TIER = 50.00
SILVER_TIER = 40.00
BRONZE_TIER = 30.00

try:
    chosen_tier = float(input("Sign up for our programing toolkit\
                             \nsubscription box and recive programing books\
                             \nt-shirts, stickers, and figurines\
                             \nWhat is your budget?> "))

    if(chosen_tier >= PLATINUM_TIER or chosen_tier > GOLD_TIER):
        print(f"Your budget of ${chosen_tier:.2f} is closest to our platinum plan which is ${PLATINUM_TIER:.2f}")

    elif(chosen_tier <= GOLD_TIER and chosen_tier > SILVER_TIER):
        print(f"Your budget of ${chosen_tier:.2f} is closest to our gold plan which is ${GOLD_TIER:.2f}")

    elif(chosen_tier < GOLD_TIER and chosen_tier > BRONZE_TIER):
        print(f"Your budget of ${chosen_tier:.2f} is closest to our silver plan which is ${SILVER_TIER:.2f}")

    elif(chosen_tier == BRONZE_TIER):
        print(f"Your budget of {chosen_tier:.2f} is closest to our bronze plan which is ${BRONZE_TIER:.2f}")

    else:
        print("Our subscription is currently out of your price range however a free trial is avaible!")

except ValueError:
    print("Invalid input!")
