# 1. ASSIGNMENT
def l_sum(l: list[float]) -> float:
    suma = 0
    for i in range(0, len(l)):
        suma += l[i]
    return suma
    """
    cislo = 0
    cislo1 = 0
    cislo2 = 0
    for i in range(0, len(l)):
            cislo = l[i]
            cislo2 = cislo1 + cislo
            cislo1 = cislo2
    return cislo1 
    """

def l_mul(l: list[float]) -> float:
    sucin = 1
    for i in range(0, len(l)):
        sucin = sucin * l[i]
    return sucin

    """
    cislo = 0
    cislo1 = 1
    cislo2 = 1
    for i in range(0, len(l)):
        cislo = l[i]
        cislo2 = cislo1 * cislo
        cislo1 = cislo2
    return cislo1 
    """


# 2. ASSIGNMENT
def is_palindrome(s: str) -> bool:
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

    """
    counter = 0
    for i in range(0, len(s) // 2):
        counter = counter + int(s[i] != s[len(s) - 1 - i])
    return counter == 0
    """

    """
    # Rovno sa moze vratit pravdivostna hodnota:
    # return counter == 0
    if counter > 0:
         return False
    else:
         return True
    """

# 3. ASSIGNMENT
def is_sum_of_digits_palindrome(s: str) -> bool:
    cislo = 0
    for i in range(0, len(s)):
        cislo += int(s[i])
    cislo = str(cislo)

    for i in range (0, len(cislo)//2):
        if (cislo[i] != cislo[len(cislo)-1-i]):
            return False
    return True


# 4. ASSIGNMENT
def remove_spaces(s: str) -> str:
    z = ''
    for i in range(0, len(s)):
        if s[i] != ' ':
            z += (s[i])
    return z

# 5. ASSIGNMENT
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    dis = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** (1/2)
    return dis 

# 6. ASSIGNMENT
def l_max(l: list[float]) -> float:
    max = l[0]
    # Float ma aj 4 necislene hodnoty, inf (nekonecno), -inf (minus nekonecno),
    # NaN (not a number, invalidne cislo) a -Nan (zaporne invalidne cislo)
    # Toto by sme pouzili, keby sme chceli spracovat aj prazdny list.
    # max = -float("inf")
    for i in range(0, len(l)):
        if l[i] > max:
            max = l[i]
    return max 

def l_min(l: list[float]) -> float:
    min = l[0]
    # min = float("inf")
    for i in range(0, len(l)):
        if l[i] < min:
            min = l[i]
    return min

def l_avg(l: list[float]) -> float:
    # if len(l) == 0:
    #     return float("NaN")
    return l_sum(l)/len(l)# remove this

# 7. ASSIGNMENT
def is_sorted(l: list[float]) -> bool:
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return False
    return True



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
my_assert('is_sorted([1]) == True')
my_assert('is_sorted([1, 2, 5, 10, 10000]) == True')
my_assert('is_sorted([-5, -1, 0, 2, 5, 10]) == True')
my_assert('is_sorted([-1, -2, 0, 2, 5, 10]) == False')
my_assert('is_sorted([3, 2, 5, 10, 10000]) == False')
my_assert('is_sorted([1, 2, 5, 10, 9]) == False')


if fail_count == 0:
    print(f"All {pass_count} tests passed! Good job!")
else:
    print(f"All tests finished. {pass_count} passed, {fail_count} failed.")
