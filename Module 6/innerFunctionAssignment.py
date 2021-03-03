"""
Program: innnerFunction
Author: Dylan Kennedy
Last date modified: 03/02/2021

The purpose of this program is to calculate the area and perimeter of a
rectangle and square.
"""

def measurments(aList):
    """
    Calculates the area and perimeter of a square or rectangle
    :params aList of atmost two different lengths.
    :returns a string representing the area and perimeter.
    """

    def area(aList):
        """
        Calculates the area of a square or rectangle.
        :params aList with at most two different lengths.
        :returns a the area.
        """
        if(len(aList) == 1):
            return aList[0] * aList[0]

        elif(len(aList) == 2):
            return aList[0] * aList[1]

        else:
            raise ValueError

    def perimeter(aList):
        """
        Calculates the perimeter of a square or rectangle.
        :params aList with at most two different lengths.
        :returns the perimeter.
        """
        if(len(aList) == 1):
            return (aList[0] + aList[0]) * 2

        elif(len(aList) == 2):
            return (aList[0] + aList[1]) * 2
        else:
            raise ValueError

    a = area(aList)
    p = perimeter(aList)
    return f"Perimeter = {p} Area = {a}"


def main():
    """
    Prints the results returned from measurments.
    :params none
    :returns result printed to the console.
    """
    try:
        rectangle = [2.1, 3.4]
        result = measurments(rectangle)
        print(result)
        square = [3.5]
        result = measurments(square)
        print(result)
        rhomboid = [2.1, 3.4, 2.7, 3.4]
        result = measurments(rhomboid)
        print(result)

    except ValueError:
        print("Can't calculate rhomboids!")


if __name__ == '__main__':
    main()
