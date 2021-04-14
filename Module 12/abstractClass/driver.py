"""
Program: driver
Author: Dylan Kennedy
Last date modified: 04/13/2021

The purpose of this program is to call each method of each subclass that
inherits from an abstract class
"""
from vehicles import Bicylce, Motorcycle, Car


if __name__ == '__main__':

    # Declare objects
    car = Car()
    bike = Bicylce()
    mototrBike = Motorcycle()

    # Print method call for each subclass.
    print(f"Power delivery for Bicylce: {bike.power_delivery()}")
    print(f"Number of passangers for Bicylce: {bike.number_passengers()}")
    print(f"Power delivery for Motorcycle: {mototrBike.power_delivery()}")
    print(f"Number of passangers for Motorcycle: {mototrBike.number_passengers()}")
    print(f"Power delivery for Car: {car.power_delivery()}")
    print(f"Number of passangers for Car: {car.number_passengers()}")
