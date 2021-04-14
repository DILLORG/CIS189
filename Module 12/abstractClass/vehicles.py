from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Calling this class Vehicle instead of rider as rider
    usually refers to the operator not the machine"""

    @abstractmethod
    def power_delivery(self):
        pass

    @abstractmethod
    def number_passengers(self):
        pass


class Bicylce(Vehicle):

    def __init__(self):
        self.power = "Human powered"
        self.min = 1
        self.max = 2

    def power_delivery(self):
        return f"{self.power}, not enclosed"

    def number_passengers(self):
        return f"{self.min} if a daredevil or {self.max} if tandem"


class Motorcycle(Vehicle):
    def __init__(self):
        self.power = "Engine powered"
        self.min = 1
        self.max = 2

    def power_delivery(self):
        return f"{self.power}, not enclosed"

    def number_passengers(self):
        return f"{self.min} or {self.max}"


class Car(Vehicle):
    def __init__(self):
        self.power = "Engine powered"
        self.min = 1
        self.max = 4

    def power_delivery(self):
        return f"{self.power}, enclosed"

    def number_passengers(self):
        return f"{self.min} to {self.max} comforably"
