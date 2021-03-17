import unittest
from dictionaryUpdate import average_scores


class TestAverageScores(unittest.TestCase):

    def test_average(self):
        scores = {'Test 1': 31, 'Test 2': 34, 'Test 3': 54}
        excpected = 39.66666666
        actual = average_scores(scores)

        self.assertAlmostEqual(excpected, actual)

    def test_average_zero(self):
        scores = {}

        with self.assertRaises(ValueError):
            average_scores(scores)

    def test_average_five(self):
        scores = {'Test 1': 5, 'Test 2': 5, 'Test 3': 5,
                  'Test 4': 5, 'Test 5': 5}
        excpected = 5
        actual = average_scores(scores)
        self.assertEqual(excpected, actual)


if __name__ == '__main__':
    unittest.main()
