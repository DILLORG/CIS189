class Quest:
    def __init__(self, name, gold, skill, dueDate):
        self.__name = name
        self.__gold = gold
        self.__skill = skill
        self.__dueDate = dueDate

    @property
    def name(self):
        return self.__name

    @property
    def gold(self):
        return self.__gold

    @property
    def skill(self):
        return self.__skill

    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, value):
        self.dueDate = value
