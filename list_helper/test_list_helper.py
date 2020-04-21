import unittest
import list_helper as lh

class TestListHelper(unittest.TestCase):
    def test_max_1(self):
        act_list = [5, 99, 27, 33, 78]
        self.assertEqual(99, lh.get_max(act_list))

    def test_max_2(self):
        act_list = [-1, 30, -50, 120, 90, -120, 0]
        self.assertEqual(120, lh.get_max(act_list))

    def test_max_3(self):
        act_list = [-30, -2, -37, -78, -10, -59]
        self.assertEqual(-2, lh.get_max(act_list))

    def test_max_4(self):
        act_list = [12, 2, 34, 5, 77, 45, 77]
        self.assertEqual(77, lh.get_max(act_list))

    def test_max_5(self):
        act_list = []
        self.assertEqual(None, lh.get_max(act_list))

    def test_shift_1(self):
        act_list = [1, 2, 3, 4]
        expected = [2, 3, 4, 1]
        lh.shift(act_list)
        self.assertEqual(expected, act_list)

    def test_shift_2(self):
        act_list = [1, 2, 3, 4]
        expected = [3, 4, 1, 2]
        lh.shift(act_list, step=2)
        self.assertEqual(expected, act_list)

    def test_shift_3(self):
        act_list = [1, 2, 3, 4, 5, 6]
        lh.shift(act_list, step=3)
        self.assertEqual([4, 5, 6, 1, 2, 3], act_list)


    def test_shift_right_1(self):
        act_list = [1, 2, 3, 4]
        expected = [4, 1, 2, 3]
        lh.shift(act_list, left=False)
        self.assertEqual(expected, act_list)

    def test_shift_right_2(self):
        act_list = [1, 2, 3, 4]
        expected = [3, 4, 1, 2]
        lh.shift(act_list, left=False, step=2)
        self.assertEqual(expected, act_list)

    def test_shift_right_3(self):
        act_list = [1, 2, 3, 4]
        lh.shift(act_list, left=False, step=3)
        self.assertEqual([2, 3, 4 , 1], act_list)

    def test_shift_right_3(self):
        act_list = [1, 2, 3, 4]
        lh.shift(act_list, left=False, step=4)
        self.assertEqual([1, 2, 3, 4], act_list)

    def test_shuffle_1(self):
        act_list = [1, 2, 3, 4]
        lh.shuffle(act_list)
        self.assertNotEqual([1, 2, 3, 4], act_list)

    def test_for_each_1(self):
        def square(val):
            return val ** 2
        act_list = [1, 2, 3, 4]
        expected = [1, 4, 9, 16]
        lh.for_each_list(act_list, square)
        self.assertEqual(expected, act_list)

    def test_for_each_2(self):
        def thirds(val):
            return val ** 3
        act_list = [0, -2, 2, 5]
        expected = [0, -8, 8, 125]
        lh.for_each_list(act_list, thirds)
        self.assertEqual(expected, act_list)

    def test_reduce_1(self):
        def sum(val1, val2):
            return val1 + val2
        act_list = [1, 2, 3, 4]
        expected = 10
        self.assertEqual(expected, lh.reduce_list(act_list, sum))

    def test_bubble_sort(self):
        act_list = [2, 3, 5, 1]
        expected = [1, 2, 3, 5]
        lh.sort_bubble(act_list)
        self.assertEqual(expected, act_list)

    def test_binary_search_1(self):
        act_list = [1, 2, 5, 7, 9, 11, 26, 89, 125, 578]
        expected = 1
        res = lh.binary_search(act_list, 2)
        self.assertEqual(expected, res)

    def test_binary_search_2(self):
        act_list = [1, 2, 5, 7, 9, 11, 26, 89, 125, 578]
        expected = -1
        res = lh.binary_search(act_list, 3)

        self.assertEqual(expected, res)

    def test_get_min_1(self):
        act_list = [1, 2, 3, -4, 5]
        expected = -4
        self.assertEqual(expected, lh.get_min(act_list))

    def test_get_sum_1(self):
        act_list = [1, 2, 3, -4, 5, 0]
        expected = 7
        self.assertEqual(expected, lh.get_sum(act_list))

    def test_remove_all_val_1(self):
        act_list = [1, 2, 3, -4, 5, 0]
        val = -4
        expected_list = [1, 2, 3, 5, 0]
        lh.remove_all_val(act_list, val)
        self.assertEqual(expected_list, act_list)

    def test_remove_all_val_2(self):
        act_list = [1, 2, 3, -4, 5, -4, 0]
        val = -4
        expected_list = [1, 2, 3, 5, 0]
        lh.remove_all_val(act_list, val)
        self.assertEqual(expected_list, act_list)

    def test_copy_list(self):
        act_list = [1, 2, 3, -4, 5, -4, 0]
        expected_list = [1, 2, 3, -4, 5, -4, 0]
        self.assertEqual(expected_list, lh.copy_list(act_list))

    def test_reverse_list(self):
        act_list = [1, 2, 3, -4, 5, -4, 0]
        expected_list = [0, -4, 5, -4, 3, 2, 1]
        self.assertEqual(expected_list, lh.remove_list(act_list))

if __name__ == '__main__':
    unittest.main()
