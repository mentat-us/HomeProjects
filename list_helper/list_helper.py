"""
#####list_helper
Common operations on lists
Works only numeric lists
"""

import random


def get_max(lst):
    """
    :param lst: (list)
    :return (int): None empty list otherwise
    max value of the list
    """
    if len(lst) == 0:
        return None
    max = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max:
            max = lst[i]
    return max

def get_min(lst):
    """
    :param lst:  (list)
    :return (int): None empty list otherwise
    min value of the list
    """
    pass


def get_sum(lst):
    """
    :param lst: (list):
    :return (int): sum of the values in the lst (numeric)
    """
    pass


def shift(lst, left=True, step=1):
    """
    :param lst: (list)
    :param left: (bool)  True if left shift False right shift (default True)
    :param step: (int)  shift count (default 1)
    :return: (None)
    shifts the values of the given list
    [1, 2, 3, 4] --> [2, 3, 4, 1]  left step 1
    [1, 2, 3, 4] --> [3, 4, 1, 2] left 2 step
    """
    temp_list = lst[0:step]

    start = 1
    stop = len(lst)


    for j in range(start, stop):
        lst[j - 1] = lst[j]


    for val in temp_list:
        lst[len(lst) - step] = val
        step -= 1

import random
def shuffle(lst):
    """
    Shuffles the list
    :param lst: (list): list that will shuffled
    :return:
    """
    N = 5
    for i in range(N):
        ind_1 = random.randint(0, len(lst) - 1)
        ind_2 = random.randint(0, len(lst) - 1)
        lst[ind_1], lst[ind_2] = lst[ind_2], lst[ind_1]


def remove_all_val(lst, val):
    """
    Removes all values from given list
    :param lst: (list):
    :param val: (int):
    :return: --
    """
    pass


def copy_list(lst):
    """
    Creates new list (shallow copy of lst
    :param lst: list
    :return list:
    """
    pass


def reverse_list(lst):
    """
    Creates new list and return reversed of lst
    :param lst: list
    :return list:
    """
    pass


def for_each_list(lst, func):
    """
    apply func to all elements of list and
    updates lst
    :param lst: (list)
    :param func : (function) func(val) return val:
    :return:
    """
    for i, val in enumerate(lst, 0):
        lst[i] = func(val)

def reduce_list(lst, func):
    """
    apply the func to list and gets the aggregeted value
    DONT change lst object
    :param lst: (list) lst:
    :param func : (function) func: func(v1, v2) returns a value
    :return: aggregated value of list
    reduce_list([1, 2, 3, 4], sum_val)
    """
    lst_1 = lst[:]
    for i in range(len(lst_1) - 1, 0, -1):
        lst_1[i - 1] = func(lst_1[i], lst_1[i - 1])
    return lst_1[0]

def sort_bubble(lst):
    """
    Sorts the list using bubble sort algorithm
    :param lst: list
    :return:
    https://youtu.be/nmhjrI-aW5o
    """
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]



def sort_selection(lst):
    """
     Sorts the list using selection sort algorithm
    :param lst: list
    :return:
    https://youtu.be/xWBP4lzkoyM
    """
    pass


def sort_range(lst, begin, end):
    """
    Sorts the list using selection sort algorithm
    in given range
    :param lst:
    :param begin: begin index inclusive
    :param end: end index exclusive
    :return:
    """
    pass


def is_sorted(lst, asc=True):
    """
    checcks the the given list ist sorted
    :param lst : (list):
    :param asc: bool checks asc or desc
    :return (bool): True if list is sorted
    otherwise return False
    """
    pass


def linear_search(lst, val):
    """
    linear search algrithm
    :param  lst: list
    :param  val: int
    :return: if val is found returns index of val
    otherwise return -1
    """
    pass


def binary_search(lst, val):
    """
    require sorted list
    linear search algrithm
    :param  lst: list
    :param  val: int
    :return: if val is found returns index of val
    otherwise return -1
    """
    start = 0
    stop = len(lst)
    while start <= stop:
        mid = (start + stop) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            stop = mid - 1
        else:
            start = mid + 1
    return -1


def fill_with_val(lst, val):
    """
    Sets list items with given val
    :param lst: list
    :param val: int
    :return:
    """
    pass


def fill_range(lst, val, begin, end):
    """
    Sets list items with given val in given range
    begin inclusive, end exculisve
    :param lst: list
    :param val: int
    :param begin: val
    :param end: val
    :return:
    """
    pass


def fill_random(lst, upper_bound, lower_bound=0):
    """
    :param lst:
    :param upper_bound:
    :param lower_bound:
    :return:
    """

    pass