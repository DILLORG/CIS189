"""
Program: assignLevel
Author: Dylan Kennedy
Last date modified: 03/16/2021

The purpose of this program is to determine the amount of points a player
recievies depending on their level.
"""


def switch_level(level):
    """
    Return the points for a given level if the level is not in the dict raise
    a ValueError.
    :params level
    :returns the points stored for that level.
    """

    level_dict = {'N': 50, 'B': 150, 'E': 300, 'A': 500}
    if level in level_dict:
        return level_dict[level]

    raise ValueError(f"{level} is not a recognized level")


def main():
    print(switch_level('N'))
    print(switch_level('B'))
    print(switch_level('F'))


if __name__ == '__main__':
    main()
