class Quest:
    def __init__(self, name, xp, skill, description, dueDate):
        self.__name = name
        self.__xp = xp
        self.__skill = skill
        self.__description = description
        self.__dueDate = dueDate

    @property
    def name(self):
        return self.__name

    @property
    def xp(self):
        return self.__xp

    @property
    def skill(self):
        return self.__skill

    @property
    def description(self):
        return self.__description

    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, value):
        self.dueDate = value
