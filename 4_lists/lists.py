# 1. ASSIGNMENT
def l_sum(l: list[float]) -> float:
    return float("inf") # remove this

def l_mul(l: list[float]) -> float:
    return float("inf") # remove this


# 2. ASSIGNMENT
def is_palindrome(s: str) -> bool:
    return False # remove this


# 3. ASSIGNMENT
def is_sum_of_digits_palindrome(s: str) -> bool:
    return False # remove this


# 4. ASSIGNMENT
def remove_spaces(s: str) -> str:
    return "\0" # remove this


# 5. ASSIGNMENT
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return float("inf") # remove this


# 6. ASSIGNMENT
def l_max(l: list[float]) -> float:
    return float("inf") # remove this

def l_min(l: list[float]) -> float:
    return float("inf") # remove this

def l_avg(l: list[float]) -> float:
    return float("inf") # remove this


# 7. ASSIGNMENT
def is_sorted(l: list[float]) -> bool:
    return False # remove this







###############################################################################
###############################################################################
################### TESTS - DO NOT MODIFY BELLOW THIS POINT ###################
###############################################################################
###############################################################################

fail_count = 0
pass_count = 0
global_pass = None

def my_assert(expression: bool):
    global fail_count
    global pass_count
    try:
        print(f"Testing  {expression}  ...", end = '')
        assert(eval(expression))
        pass_count += 1
        print("Passed")
    except AssertionError as e:
        fail_count += 1
        print("Failed")

my_assert('l_sum([45]) == 45')
my_assert('l_sum([6, 9]) == 15')
my_assert('l_sum([5, 4, 42, 4, 12, 45, 48, 123, 47]) == 330')
my_assert('l_sum([4, 5, 2, 45, 845, 21, 3, 45, 6, 5, 1, 54, 123, 45, 12]) == 1216')

my_assert('l_mul([45]) == 45')
my_assert('l_mul([4, 5]) == 20')
my_assert('l_mul([5, 4, 7, 8, 5, 21, 4]) == 470400')
my_assert('l_mul([4, 45, 2, 3, 4, 74, 45]) == 14385600')
my_assert('l_mul([45, 4, 12, 45, 78, 54, 34]) == 13919817600')

my_assert('is_palindrome("abba") == True')
my_assert('is_palindrome("abcba") == True')
my_assert('is_palindrome("abcdcba") == True')
my_assert('is_palindrome("abdcba") == False')
my_assert('is_palindrome("abccbb") == False')
my_assert('is_palindrome("abcdcbb") == False')
my_assert('is_palindrome(" abcdcba ") == True')
my_assert('is_palindrome(" abcddcba ") == True')

my_assert('is_sum_of_digits_palindrome("0") == True')
my_assert('is_sum_of_digits_palindrome("1") == True')
my_assert('is_sum_of_digits_palindrome("56") == True')
my_assert('is_sum_of_digits_palindrome("65") == True')
my_assert('is_sum_of_digits_palindrome("121") == True')
my_assert('is_sum_of_digits_palindrome("949") == True')
my_assert('is_sum_of_digits_palindrome("333336666666441") == True')
my_assert('is_sum_of_digits_palindrome("9999555774444448888") == True')
my_assert('is_sum_of_digits_palindrome("55") == False')
my_assert('is_sum_of_digits_palindrome("424") == False')

my_assert('remove_spaces("abcd") == "abcd"')
my_assert('remove_spaces("a b c d") == "abcd"')
my_assert('remove_spaces("a   b") == "ab"')
my_assert('remove_spaces(" a  b  c ") == "abc"')
my_assert('remove_spaces(" a  b    c ") == "abc"')
my_assert('remove_spaces("        ") == ""')
my_assert('remove_spaces(" a b c d e ") == "abcde"')

# This checks whether the original string was modified
global_pass = " a b c d e "
my_assert('remove_spaces(global_pass) == "abcde"')
my_assert('global_pass == " a b c d e "')

my_assert('distance(0, 7, 0, 7) == 0')
my_assert('distance(0, 0, 10, 0) == 10')
my_assert('distance(0, -20, 10, -20) == 10')
my_assert('abs(distance(0, 0, 5, 4) - 6.40) < 0.01')
my_assert('abs(distance(123, -451, 12, 123) - 584.63) < 0.01')
my_assert('abs(distance(-13, -451, 12, 123) - 574.54) < 0.01')
my_assert('distance(3, 6, 7, 9) == 5')

my_assert('l_max([1, 2, 3]) == 3')
my_assert('l_max([5]) == 5')
my_assert('l_max([6, 7, 5]) == 7')
my_assert('l_max([10, 7, 5]) == 10')
my_assert('l_max([-10, -7, -5]) == -5')

my_assert('l_min([1, 2, 3]) == 1')
my_assert('l_min([5]) == 5')
my_assert('l_min([6, 5, 7]) == 5')
my_assert('l_min([10, 7, 5]) == 5')
my_assert('l_min([-10, -7, -5]) == -10')

my_assert('l_avg([1, 2, 3]) == 2')
my_assert('l_avg([5]) == 5')
my_assert('l_avg([6, 5, 10]) == 7')
my_assert('l_avg([11, 8, 5]) == 8')
my_assert('l_avg([-10, -7, -4]) == -7')
my_assert('l_avg([-10, -7, -4, 4]) == -4.25')
my_assert('l_avg([42, 45, -62, -6, 24, -266, -8, 3]) == -28.5')

my_assert('is_sorted([1, 2, 3]) == True')
my_assert('is_sorted([2, 2, 2]) == True')
my_assert('is_sorted([1, 2, 5, 10, 10000]) == True')
my_assert('is_sorted([-5, -1, 0, 2, 5, 10]) == True')
my_assert('is_sorted([-1, -2, 0, 2, 5, 10]) == False')
my_assert('is_sorted([3, 2, 5, 10, 10000]) == False')
my_assert('is_sorted([1, 2, 5, 10, 9]) == False')


if fail_count == 0:
    print(f"All {pass_count} tests passed! Good job!")
else:
    print(f"All tests finished. {pass_count} passed, {fail_count} failed.")
