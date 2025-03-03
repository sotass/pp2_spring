from functools import reduce
import time
import math

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)


def count_upper_lower(s):
    upper = sum(1 for char in s if char.isupper())
    lower = sum(1 for char in s if char.islower())
    return upper, lower


def is_palindrome(s):
    return s == s[::-1]


def delayed_sqrt(number, delay_ms):
    time.sleep(delay_ms / 1000)
    return math.sqrt(number)


def all_true(tpl):
    return all(tpl)

print("Multiply list:", multiply_list([1, 2, 3, 4]))
print("Upper and Lower case count:", count_upper_lower("Hello World!"))
print("Is palindrome:", is_palindrome("madam"))
print("Square root after delay:", delayed_sqrt(25100, 2123))
print("All elements True:", all_true((True, True, False)))