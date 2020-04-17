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
    if not lst:
        return None
    max = lst[0]
    for val in lst:
        if val > max:
            max = val
    return max


def get_min(lst):
    """
    :param lst:  (list)
    :return (int): None empty list otherwise
    min value of the list
    """
    if not lst:
        return None
    min = lst[0]
    for val in lst:
        if val < min:
            min = val
    return min


def get_sum(lst):
    """
    :param lst: (list):
    :return (int): sum of the values in the lst (numeric)
    """
    sum = 0
    for val in lst:
        sum += val
    return sum


def shift(lst, left=True, step=1):
    """
    :param lst: (list)
    :param left: (bool)  True if left shift False right shift (default True)
    :param step: (int)  shift count (default 1)
    :return: (None)
    shifts the values of the given list
    """
    temp = lst[0: step] if left else lst[-step:]

    #start = step if left else len(lst) - step - 1
    #stop = len(lst) if left else len(lst) - step - 1

    start = 1
    stop = len(lst) - step

    for i in range(start, stop):
        lst[i - 1] = lst[i]

    #TODO: assign temp list to lst


def shuffle(lst):
    """
    Shuffles the list
    :param lst: (list): list that will shuffled
    :return:
    """
    count = 100
    for i in range(count):
        f = random.randrange(0, len(lst))
        e = random.randrange(0, len(lst))
        lst[f], lst[e] = lst[e], lst[f]


def remove_all_val(lst, val):
    """
    Removes all values from given list
    :param lst: (list):
    :param val: (int):
    :return: --
    """
    count = lst.count(val)
    while count > 0:
        lst.remove(val)
        count -= 1


def copy_list(lst):
    """
    Creates new list (shallow copy of lst
    :param lst: list
    :return list:
    """
    return lst[:]


def reverse_list(lst):
    """
    Creates new list and return reversed of lst
    :param lst: list
    :return list:
    """
    return lst[::-1]


def for_each_list(lst, func):
    """
    apply func to all elements of list and
    updates lst
    :param lst: (list)
    :param func : (function) func(val) return val:
    :return:
    """
    for i, val in enumerate(lst):
        lst[i] = func(val)


def reduce_list(lst, func):
    """
    apply the func to list and gets the aggregeted value
    :param lst: (list) lst:
    :param func : (function) func: func(v1, v2) returns a value
    :return: aggregated value of list
    reduce_list([1, 2, 3, 4], sum_val)
    """
    temp_list = lst
    for i in range(len(temp_list) - 1, -1, -1 ):
        temp_list[i - 1] = func(temp_list[i], temp_list[i - 1])

    res = temp_list[0]
    return res;


def sort_bubble(lst):
    """
    Sorts the list using bubble sort algorithm
    :param lst: list
    :return:
    https://youtu.be/nmhjrI-aW5o
    """
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def sort_selection(lst):
    """
     Sorts the list using selection sort algorithm
    :param lst: list
    :return:
    https://youtu.be/xWBP4lzkoyM
    """
    for i in range(len(lst)):
        min_idx = i
        for j in range(i  + 1, len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]


def sort_range(lst, begin, end):
    """
    Sorts the list using selection sort algorithm
    in given range
    :param lst:
    :param begin: begin index inclusive
    :param end: end index exclusive
    :return:
    """
    for i in range(begin, end):
        min_idx = i
        for j in range(i  + 1, end):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[min_idx], lst[i] = lst[i], lst[min_idx]


def is_sorted(lst, asc=True):
    """
    checcks the the given list ist sorted
    :param lst : (list):
    :param asc: bool checks asc or desc
    :return (bool): True if list is sorted
    otherwise return False
    """

    def is_asc(): #v1 < v2
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    def is_desc(): #v1 > v2
        for i in range(len(lst) - 1):
            if lst[i] < lst[i + 1]:
                return False
        return True

    return is_asc() if asc else is_desc()


def linear_search(lst, val):
    """
    linear search algrithm
    :param  lst: list
    :param  val: int
    :return: if val is found returns index of val
    otherwise return -1
    """
    for i, item in enumerate(lst):
        if item == val:
            return i
    return -1


def binary_search(lst, val):
    """
    require sorted list
    linear search algrithm
    :param  lst: list
    :param  val: int
    :return: if val is found returns index of val
    otherwise return -1
    """
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] == val:
            return mid
        elif lst[mid] > val:
            high = mid
        else:
            low = mid
    return -1


def fill_with_val(lst, val):
    """
    Sets list items with given val
    :param lst: list
    :param val: int
    :return:
    """
    for i in range(len(lst)):
        lst[i] = val


def fill_range(lst, val, begin, end):
    """
    Sets list items with given val in given range
    :param lst: list
    :param val: int
    :param begin: val
    :param end: val
    :return:
    """
    for i in range(begin, end):
        lst[i] = val


def fill_random(lst, upper_bound, lower_bound=0):
    """
    
    :param lst:
    :param upper_bound:
    :param lower_bound:
    :return:
    """
    for i in range(len(lst)):
        lst[i] = random.randrange(lower_bound, upper_bound)
