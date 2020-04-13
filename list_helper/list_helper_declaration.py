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
    pass


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
    """
    pass


def shuffle(lst):
    """
    Shuffles the list
    :param lst: (list): list that will shuffled
    :return:
    """
    pass


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
    pass


def reduce_list(lst, func):
    """
    apply the func to list and gets the aggregeted value
    :param lst: (list) lst:
    :param func : (function) func: func(v1, v2) returns a value
    :return: aggregated value of list
    reduce_list([1, 2, 3, 4], sum_val)
    """
    pass


def sort_bubble(lst):
    """
    Sorts the list using bubble sort algorithm
    :param lst: list
    :return:
    https://youtu.be/nmhjrI-aW5o
    """
    pass


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
    pass


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