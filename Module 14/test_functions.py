from camper_age_input import convert_to_months
import unittest


class TestConvertToMonths(unittest.TestCase):

    def test_good_input_min_age(self):
        expected = 12
        actual = convert_to_months('1')
        self.assertEqual(expected, actual)

    def test_good_input_max_age(self):
        expected = 60
        actual = convert_to_months('5')
        self.assertEqual(expected, actual)

    def test_bad_input_range(self):
        with self.assertRaises(ValueError):
            convert_to_months('55')

    def test_bad_input_type(self):
        with self.assertRaises(ValueError):
            convert_to_months('t')


if __name__ == '__main__':
    unittest.main()
