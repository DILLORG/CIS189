import unittest
from game.numberGuesser import NumberGuesser


class TestGame(unittest.TestCase):
    def setUp(self):

        self.min = 1
        self.max = 10
        self.amount = 9
        self.numberGuesser = NumberGuesser(self.min, self.max, self.amount)

    def tearDown(self):
        del self.numberGuesser

    def test_add_guess_bad_values(self):
        """
        Test that non numeric guesses and guesses not within
        the range raise value errors
        """

        with self.assertRaises(ValueError):
            self.numberGuesser.add_guess(100)

        with self.assertRaises(ValueError):
            self.numberGuesser.add_guess(-1)

        with self.assertRaises(ValueError):
            self.numberGuesser.add_guess("S")

    def test_winner_bad_index(self):
        """
        Test that either a index out of range or a non numeric throws an error.
        """

        with self.assertRaises(ValueError):
            self.numberGuesser.force_winner("8t")

        with self.assertRaises(IndexError):
            self.numberGuesser.force_winner(self.max + 1)

    def test_winner(self):
        """
        Typically the winning number is generated
        during the call to the constructor here we force the
        winning number to a given index to test that a win is possible.
        """

        # No winner
        self.assertFalse(self.numberGuesser.is_winner())

        self.numberGuesser.force_winner(3)
        self.assertTrue(self.numberGuesser.is_winner())


if __name__ == '__main__':
    unittest.main()
