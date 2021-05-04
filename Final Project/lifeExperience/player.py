from .quest import Quest
from .exceptions import DuplicateQuestError
from .exceptions import QuestExistError
from .exceptions import DuplicateSkillError
from .exceptions import SkillExistError
from .exceptions import ShopItemExistError


class Player:
    """
    Class to represent players profile
    Attributes:
    name -- Player's name.
    difficulty -- How difficult it is for the player to level up
    skillLevel -- Holds all players skills and their current level.
    quest -- Holds all players assined quest.
    """

    def __init__(self, name, type, difficulty=1):
        """
        Constructs Player Object.
        :params players name and difficulty
        """
        self.__name = name
        self.__type = type
        self.__difficulty = difficulty
        self.__skillLevel = {'Player': 0}
        self.__quests = {}
        self.__shop = {}
        self.__gold = 0

    @property
    def name(self):
        return self.__name

    @property
    def type(self):
        return self.__name

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def skills(self):
        return self.__skillLevel

    @property
    def quests(self):
        return self.__quests

    @property
    def shop(self):
        return self.__shop

    @property
    def gold(self):
        return self.__gold

    def add_quest(self, questName, xp, skill, description, dueDate):
        """
        Assign a new quest to the player. IF a quest with the same name
        is already assined to the player raise an error.
        :params questName, xp, skill, description, dueDate
        """

        if questName in self.__quests.keys():
            raise DuplicateQuestError(f"{questName} is already an assined Quest")

        quest = Quest(questName, xp, skill, description, dueDate)
        self.__quests.update({questName: quest})

    def complete_quest(self, questName):
        """
        Complete an active quest add experienc points to
        the related skill. IFf the quest isn't currently assined raise an
        error.
        :params quest name.
        :returns none.
        """
        if questName not in self.__quests.keys():
            raise QuestExistError(f"{questName} is not an assined Quest")

        quest = self.__quests.pop(questName)
        self.__skillLevel[quest.skill] += quest.xp
        self.__skillLevel['Player'] += (1 * self.__difficulty)

    def add_gold(self, value):
        self.__gold += value

    def add_shop_item(self, itemName, price):
        self.__shop.update({itemName: price})

    def purchase_shop_item(self, itemName):
        if itemName not in self.__shop.keys():
            raise ShopItemExistError(f"{itemName} has not been added")

        self.__gold -= self.__shop[itemName]

    def add_skill(self, skillName):
        """
        Add a skill. If the skill already exist return an error.
        :params skillName
        :returns none.
        """
        if skillName in self.__skillLevel.keys():
            raise DuplicateSkillError(f"{skillName} has already been added")

        self.__skillLevel.update({skillName: 0})

    def get_skill_level(self, skillName):
        """
        Get the current skill level of a given skill. throw an error if
        the skill doesn't exist.
        :params skillName
        :returns skillLevel
        """
        if skillName not in self.__skillLevel.keys():
            raise SkillExistError(f"{skillName} is not a skill")

        return self.__skillLevel[skillName]

    def __str__(self):
        return f"Player({self.__name}, {self.__skillLevel}, {self.__quests.keys()})"

    def __repr__(self):
        return f"'Player({self.__name}, {self.__skillLevel}, {self.__quests.keys()})'"
