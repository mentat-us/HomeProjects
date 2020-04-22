def reverse_string(s):
    """
    reverses the given string
    :type s: [str]
    :rtype: str.
    """
    res_str = ""
    for i in range(len(s) - 1, -1, -1):
        res_str += s[i]
    return res_str
    #shortly slicing :)
    #return s[::-1]

def is_palindrome(s):
    """
    :param s: str
    :return: bool if its palindrome
    """
    for i in range(len(s) // s):
        if s[i] != s[len(s) - 1 - i]:
            return False

    return True

def is_integer(s):
    s = s.strip()
    if (s[0] == "+" or s[0] == "-") and s[1:].isdigit():
        return True
    if s.isdigit():
        return True
    return False


def to_integer(s):
    """
    check the str contains - sign
    :param s:
    :return:
    """
    if not is_integer(s):
        return None

    sign = 1
    if s.startswith("+") or s.startswith("-"):
        if s.startswith("-"):
            sign = -1
        s = s[1:]


    int_val = 0
    for i, val in enumerate(reversed(s)):
        int_val += (ord(val) - ord("0")) * 10 ** i

    return sign * int_val



def hex_to_dec(s):
    """
    hexadecimal digits (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E and F)
    and decimal (base 10) integers
    :param s: (str)
    :return: (int)
    """
def dec_to_hex():
    """
    int2hex function is responsible
    for converting an integer between 0 and 15 to a single hexadecimal digit.
    :return:
    """
def double_char(txt):
    """
    Create a function that takes a string and returns a
    string in which each character is repeated once.
    :param txt: str
    :return: str
    hello --> hheelloo
    """
    result = ''
    for t in txt:
        result += t * 2
    return result


def sort_chars(txt):
    """Create a function that takes a
    string and returns a string
    with its letters in alphabetical order.
    :param txt: str
    :return: str
    hello --> ehllo
    """

def is_vowel(ch):
    """

    :param ch: str
    :return: bool
    """

def count_vowels(txt):
    """
    Create a function that takes a string and returns
    the number(count) of vowels contained
    within it.
    :param txt:
    :return:
    """

def count_consonant(s):
    """
    Create a function that takes a string and returns
    the number(count) of consonant contained
    within it.
    :param s:str
    :return:
    hint create is_vowel func
    """


def inverse_case(s):
    """
    Convert all lowercase letters to uppercase letters and vice versa
    :param s:
    :return:
    """
    res = ""
    for c in s:
        if c.islower():
            res += c.upper()
            continue
        res += c.lower()
    return res


def is_isogram(txt):
    """
    An isogram is a word that has no repeating letters, consecutive or nonconsecutive.
    Create a function that takes a string and returns either
    True or False depending on whether or not it's an "isogram".
    :param txt: str
    :return:bool
    is_isogram("Algorism") ➞ True
    is_isogram("PasSword") ➞ False
    is_isogram("Consecutive") ➞ False
    """

def checkPassword(password):
    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True

    return False