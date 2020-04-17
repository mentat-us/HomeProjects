import unittest as ut
#from list_helper import list_helper as lh
from list_helper.solutions import list_helper as lh

class ListHelperTester(ut.TestCase):

    '''def setUp(self):
        pass
    def tearDown(self):
        pass
    '''
    def test_max(self):
        test_list = [10, 52, 99, 56, 5, 4, 22, 17, 52, 23]
        self.assertEqual(99, lh.max(test_list))

    #left 1 step
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

    def test_shuffle_1(self):
        act_list = [1, 2, 3, 4, 5, 6]
        lh.shuffle(act_list)
        self.assertNotEqual([1, 2, 3, 4, 5, 6], act_list)

    def test_remove_all_val(self):
        act_list = [1, 2, 2, 4, 2, 6]
        lh.remove_all_val(act_list, 2)
        self.assertEqual([1, 4, 6], act_list)

    def test_copy_list(self):
        act_list = [-1, 2, 3, 4, 5, -6]
        copied_list = lh.copy_list(act_list)
        self.assertEqual(copied_list, act_list)
        self.assertNotEqual(id(act_list), id(copied_list))

    def test_reverse_list(self):
        act_list = [1, 2, 2, 4, 2, 6]
        expected_list = [6, 2, 4, 2, 2, 1]
        self.assertEqual(expected_list, lh.reverse_list(act_list))

    def test_for_each_list(self):
        def m_square(x):
            return x ** 2
        lst = [10, 20, 30]
        lh.for_each_list(lst, m_square)
        self.assertEqual([100, 400, 900], lst)

    def test_reduce_list_1(self):
        def sum(v1, v2):
            return v1 + v2

        lst = [10, 20, 30]
        self.assertEqual(60, lh.reduce_list(lst, sum))

    def test_reduce_list_2(self):
        def multip(v1, v2):
            return v1 * v2

        lst = [10, 20, 30]
        self.assertEqual(6_000, lh.reduce_list(lst, multip))

    def test_bubble_sort(self):
        lst = [8, 6, 7, 1, 9, 2, 4, 3, 5]
        lh.sort_bubble(lst)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], lst)

    def test_selection_sort(self):
        lst =  [8, 6, 7, 1, 9, 2, 4, 3, 5]
        lh.sort_selection(lst)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], lst)

    def test_sort_range(self):
        lst = [8, 6, 7, 1, 9, 2, 4, 3, 5]
        lh.sort_range(lst, 2, 5)
        self.assertEqual([8, 6, 1, 7, 9, 2, 4, 3, 5], lst)

    def test_is_sorted_asc(self):
        self.assertTrue(lh.is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_is_sorted_desc(self):
        self.assertTrue(lh.is_sorted([9, 8, 7, 6, 5, 4, 3, 2, 1], False))


'''neden olmuyor
lst = [0] * 10
print("10 eleman girin")
for i in range(0,10,1):
    lst[i] = eval(input(str(i+1) + ".değeri giriniz"))
print(lst)
'''
if __name__ == '__main__':
    ut.main()