from .quest import Quest
from .exceptions import DuplicateQuestError
from .exceptions import QuestExistError
from .exceptions import DuplicateSkillError
from .exceptions import SkillExistError
from .exceptions import ShopItemExistError
from .exceptions import NotEnoughGoldError


class Player:
    """
    Class to represent players profile
    Attributes:
    name -- Player's name.
    difficulty -- How difficult it is for the player to level up
    skillLevel -- Holds all players skills and their current level.
    quest -- Holds all players assined quest.
    """

    def __init__(self, name='', type=''):
        """
        Constructs Player Object.
        :params players name and difficulty
        """
        self.__name = name
        self.__level = 1
        self.__type = type
        self.__skills = []
        self.__quests = []
        self.__shop = []
        self.__gold = 0

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def quests(self):
        return self.__quests

    @quests.setter
    def quests(self, value):
        self.__quests = value

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, value):
        self.__skills = value

    @property
    def shop(self):
        return self.__shop

    @shop.setter
    def shop(self, value):
        self.__shop = value

    @property
    def gold(self):
        return self.__gold


    def add_gold(self, value):
        self.__gold += value

    def remove_gold(self, value):
        if value > self.__gold:
            raise NotEnoughGoldError
        self.__gold -= value

    def __str__(self):
        return f"Player({self.__name}, {self.__skill}, {self.__quests})"

    def __repr__(self):
        return f"'Player({self.__name}, {self.__skills}, {self.__quests.keys()})'"
