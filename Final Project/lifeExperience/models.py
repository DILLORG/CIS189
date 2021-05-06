import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .exceptions import DuplicateSkillError, DuplicateQuestError
from .exceptions import SkillExistError, QuestExistError, ShopItemExistError


class SkillListStore(Gtk.ListStore):
    def __init__(self):
        Gtk.ListStore.__init__(self, str, int)

    def add_skill(self, name):
        for row in self:
            if row[0] == name:
                raise DuplicateSkillError(f"Skill {name} already added")

        self.append([name, 0])

    def add_points_to_skill(self, name, value):
        for row in self:
            if row[0] == name:
                row[1] += value

    def get_skill(self, name):
        for row in self:
            if row[0] == name:
                return row[0][1]
        raise SkillExistError(f"Skill {name} not in skills")


class QuestListStore(Gtk.ListStore):
    def __init__(self):
        Gtk.ListStore.__init__(self, str, int, str, str)

    def add_quest(self, name, gold, skill, dueDate):
        for row in self:
            if row[0] == name:
                raise DuplicateQuestError(f"Quest {name} already added")

        self.append([name, gold, skill, dueDate])

    def get_quest(self, name):
        for row in self:
            if row[0] == name:
                return row[0][1][2][3]
        raise QuestExistError(f"Quest {name} is not one of your quest")


class ShopListStore(Gtk.ListStore):
    def __init__(self):
        Gtk.ListStore.__init__(self, str, int)

    def add_item(self, name, price):
        self.append([name, price])

    def get_item(self, name):
        for row in self:
            if row[0] == name:
                return row[0][1]

        raise ShopItemExistError(f"{name} not found")
