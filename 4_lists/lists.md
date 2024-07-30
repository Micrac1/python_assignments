# Lists

Use the `lists.py` as your starting point. It contains not only function
skeletons, but also a **bunch of tests**. Use them to make sure your functions
are correct!

In order to run the tests, run the `lists.py` file. You should see which test
is being run and whether it passed or failed.

Do not edit anything other than the functions specified in the assignments.

## 1. Sum of all parts (and multiple)

Implement functions `l_sum` and `l_mul`.

The `l_sum`/`l_mul` function takes a non-empty list of numbers as an
argument, adds/multiplies the numbers together and returns the result.

**Do not use the built-in `sum()` function!**

You can assume that the input list is always valid and has at least 1
number in it.

## 2. Level aibohphobia

Implement the `is_palindrome` function. The function takes a string as an
argument and returns `True` if the string is a palindrome, `False` otherwise.

## 3. Wow, rotator level

Implement the `is_sum_of_digits_palindrome` function. The function takes a
**string** as an argument and returns `True` if the sum of all digits in the
string is a palindrome, `False` otherwise.

You can reuse the `is_palindrome` function from the previous excersise.

You can assume that the input string contains only `0123456789` characters.

## 4. I need some S P A C E (or not)

Implement the `remove_spaces` function. The function takes a string as an
argument and returns **a new string**, identical to the argument, but with all
spaces removed.

**Make sure that the original string is not modified!**

## 5. The distance in your eyes...

Implement the `distance` function. The function takes 2 2D coordinates (4
numbers in total) as arguments and returns the distance between them.

## 6. Maximus, Minimus and their brother Avergus

Implement the `l_max`, `l_min` and `l_avg` functions. The functions take
a list of numbers as an argument and return the maximum/minimum/average value
of the input list.

**Do not use the built-in `max()` and `min()` functions!**

You can assume that the input list always has at least 1 number in it.

## 7. Order in the room!

Implement the `is_sorted` function. The function takes a list of numbers as an
argument and returns `True` if the numbers in the list are
sorted from the smallest to largest, `False` otherwise.

There **can** be duplicate numbers, for example `[1, 2, 2, 3]` is a
sorted list.
