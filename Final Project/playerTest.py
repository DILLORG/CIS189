from lifeExperience.player import Player
from lifeExperience.models import SkillListStore, QuestListStore, ShopListStore
from lifeExperience.exceptions import DuplicateQuestError, DuplicateSkillError
from lifeExperience.exceptions import QuestExistError, SkillExistError
from lifeExperience.exceptions import ShopItemExistError
from lifeExperience.exceptions import NotEnoughGoldError
from pickle import load, dump
import unittest


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.testPlayer = Player('Dylan', 'Programer')
        self.testSkillList = SkillListStore()
        self.testQuestList = QuestListStore()
        self.testShopList = ShopListStore()
        self.testSkillList.add_skill('Programing')
        self.testQuestList.add_quest('Finish Final', 500, 'Programing', '05-06-2021 23:59')

    def tearDown(self):
        del self.testPlayer
        del self.testSkillList
        del self.testQuestList
        del self.testShopList

    def test_add_skill_exist(self):
        with self.assertRaises(DuplicateSkillError):
            self.testSkillList.add_skill('Programing')

    def test_get_skill_doesnt_exist(self):
        with self.assertRaises(SkillExistError):
            self.testSkillList.get_skill('Gardening')

    def test_add_quest_exist(self):
        with self.assertRaises(DuplicateQuestError):
            self.testQuestList.add_quest('Finish Final', 500, 'Programing', '05-06-2021 23:59')

    def test_get_quest_doesnt_exist(self):
        with self.assertRaises(QuestExistError):
            self.testQuestList.get_quest('Clean Room')

    def test_player_too_little_gold(self):
        with self.assertRaises(NotEnoughGoldError):
            self.testPlayer.remove_gold(500)

    def test_get_shop_doesnt_exist(self):
        with self.assertRaises(ShopItemExistError):
            self.testShopList.get_item('Banana')

    def test_player_save_profile(self):
        fileName = 'playerTest.data'

        with open(fileName, 'wb') as file:
            dump(self.testPlayer, file)

        with open(fileName, 'rb') as file:
            newPlayer = load(file)

        self.assertEqual(repr(self.testPlayer), repr(newPlayer))
        self.assertEqual(str(self.testPlayer), str(newPlayer))


if __name__ == '__main__':
    unittest.main()
