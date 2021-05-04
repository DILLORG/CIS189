class DuplicateSkillError(Exception):
    def __init__(self, message="Skill already exist"):
        self.messge = message
        super().__init__(self.messge)


class SkillExistError(Exception):
    def __init__(self, message="Skill doesn't exist"):
        self.message = message
        super().__init__(self.message)


class DuplicateQuestError(Exception):
    """
    Exception that is raise when we attempt to add a duplicate quest
    Attributes:
    message -- An explanation of the error.
    """

    def __init__(self, message="Quest has already been added"):
        self.message = message
        super().__init__(self.message)


class QuestExistError(Exception):

    def __init__(self, message="Quest has not been added"):
        self.message = message
        super().__init__(self.message)


class ShopItemExistError(Exception):
    """
    Exception that is raised when attempt to purchase an item that doesn't
    exist.
    Attributes:
    message -- An explanation of the error.
    """

    def __init__(self, message="Item has not been added"):
        self.message = message
        super().__init__(self.message)


class NotEnoughGoldError(Exception):
    """
    Exception that is raised when attempt to purchase item without the
    required gold.
    Attributes:
    message -- An explanation of the error.
    """
    def __init__(self, message="Item is to expensive"):
        self.message = message
        super().__init__(self.message)
