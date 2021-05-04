from lifeExperience.player import Player
from lifeExperience.exceptions import DuplicateQuestError, DuplicateSkillError
from lifeExperience.exceptions import QuestExistError, SkillExistError
from lifeExperience.exceptions import ShopItemExistError
from pickle import load, dump
import unittest


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.testPlayer = Player('Dylan', 'Programer')
        self.testPlayer.add_skill('Strength')
        self.testPlayer.add_quest('Excersise', 500, 'Strength', 'Go Excersise', '01-01-01')
        self.testPlayer.add_quest('Walk', 50, 'Strength', 'Go for a walk', '01-01-01')
        self.testPlayer.complete_quest('Walk')

    def tearDown(self):
        del self.testPlayer

    def test_player_add_quest_duplicate(self):
        with self.assertRaises(DuplicateQuestError):
            self.testPlayer.add_quest('Excersise', 500, 'Strength', 'Go Excersise', '01-01-01')

    def test_player_add_skill_duplicate(self):
        with self.assertRaises(DuplicateSkillError):
            self.testPlayer.add_skill('Strength')

    def test_player_add_skill(self):
        self.testPlayer.add_skill('Art')
        expected = 0
        actual = self.testPlayer.get_skill_level('Art')
        self.assertEqual(expected, actual)

    def test_get_skill_level_no_skill(self):
        with self.assertRaises(SkillExistError):
            self.testPlayer.get_skill_level('Math')

    def test_player_complete_quest_no_quest(self):
        with self.assertRaises(QuestExistError):
            self.testPlayer.complete_quest('Take Out Trash')

    def test_player_complete_quest(self):
        self.testPlayer.complete_quest('Excersise')
        expected = 550
        actual = self.testPlayer.get_skill_level('Strength')
        self.assertEqual(expected, actual)

    def test_add_shop_item_no_item(self):

        with self.assertRaises(ShopItemExistError):
            self.testPlayer.purchase_shop_item('Guitar')


    def test_player_save_profile(self):
        fileName = 'playerTest.profile'

        newPlayer = Player()
        with open(fileName, 'wb') as file:
            dump(newPlayer, file)

        with open(fileName, 'rb') as file:
            newPlayer = load(file)

        self.assertEqual(repr(self.testPlayer), repr(newPlayer))
        self.assertEqual(str(self.testPlayer), str(newPlayer))


if __name__ == '__main__':
    unittest.main()
