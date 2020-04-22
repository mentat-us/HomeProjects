def find_max_consecutive_ones(nums):
    """
    Given a binary list(only contain 0 and 1),
    find the maximum number of consecutive 1s in this list.
    :type nums: List[int]
    :rtype: int
    Input: [1,1,0,1,1,1]
    Output: 3 (last three 1s)
    """

    i = 0
    one_counter = 0;
    while i < len(nums):
        temp_counter = 0
        if nums[i] == 0:
            i += 1
            continue
        while i < len(nums) and nums[i] == 1:
            temp_counter += 1
            i += 1

        if temp_counter > one_counter:
            one_counter = temp_counter

    return one_counter

def find_digit_counts(nums):
    """
    Given an list nums of integers,
    return new list contain number of digits
    respectivly
    :type nums: List[int]
    :rtype: list
    """
    def get_digit_count(val):
        if val == 0:
            return 1
        count = 0
        while val > 0:
            val //= 10
            count += 1

        return count

    return [get_digit_count(v) for v in nums]

def duplicate_zeros(nums):
    """
    Given a fixed length array arr of integers,
     duplicate each occurrence of zero, shifting the remaining elements to the right.
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    Input: [1,0,2,3,0,4,5,0]
    Output: None
    Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
    Input: [1,2,3]
    Output: null
    Explanation: After calling your function, the input array is modified to: [1,2,3]
    """

def remove_duplicates(nums):
    """
    Given a sorted array nums, remove the duplicates in-place such that
    each element appear only once and return the new length.
    :type nums: List[int]
    :rtype: int
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    0our function should return length = 5, with the first five elements of nums
    being modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.
    """

def merge(nums1, nums2):
    """
    Given two sorted int list nums1 and nums2, merge nums2 into nums1 as one sorted array.
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    nums1 = [1,2,3]
    nums2 = [2,5,6]
    [1,2,2,3,5,6]
    """

def valid_mountain_array(nums):
    """
    Given an list lst of integers,
    return true if and only if it is a valid mountain array.
    (first strictly incresing and than strictly decreasing
    :type nums: List[int]
    :rtype: bool
    Input: [2,1]
    Output: false
    Input: [3,5,5]
    Output: false
    Input: [0,3,2,1]
    Output: true
    """
