import unittest
import play_with_list as pwt


class TestPlayWithList(unittest.TestCase):
    def test_max_consecutive_ones_1(self):
        self.assertEqual(3, pwt.find_max_consecutive_ones([1, 1, 0, 0, 1, 1, 1, 0]))

    def test_max_consecutive_ones_2(self):
        self.assertEqual(5, pwt.find_max_consecutive_ones([0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0]))

    def test_max_consecutive_ones_3(self):
        self.assertEqual(9, pwt.find_max_consecutive_ones([1, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_max_consecutive_ones_4(self):
        self.assertEqual(0, pwt.find_max_consecutive_ones([0, 0, 0, 0, 0, 0, 0, 0, 0]))

    def test_max_consecutive_ones_5(self):
        self.assertEqual(0, pwt.find_max_consecutive_ones([]))

    def test_find_digit_counts(self):
        self.assertEqual([2, 3, 1, 1, 4, 1], pwt.find_digit_counts([12, 123, 1, 0, 1234, 5]))


if __name__ == '__main__':
    unittest.main()
