import sys

# 1. Do funkcie print_tree pridat treti argument: pocet roznych typov stromcekov,
# ktore sa budu vykrelovat. Pouzije pole char.

# 2. Zmenit kod na vypisovanie kmenov tak, aby sedeli so stromcekami.
# Pripadne pridat rozne znaky iba pre kmene

spac: str = ' '
char: list[str] = ['#', '%', '^', '&', '$', '*', '-']

def print_tree(line_count, tree_count, tree_types):
    # char_red = char[:tree_types] ZLE ZLE ZLE
    char_current = char[0]
    if tree_types > len(char):
       # Moc genericke, chceme co najspecifickejsi exception, aby uzivatel vedel
       # co najpresnejsie info
       # raise Exception(f"tree_types can not be more than {len(char)}")
       raise ValueError(f"tree_types can not be more than {len(char)}")
    if tree_types < 1:
       raise ValueError(f"tree_types can not be less than 1")

    # Print the leaves
    for cur_line in range(0, line_count):
        for cur_tree in range(0, tree_count):
            # print leading spaces
            print((line_count - 1 - cur_line) * spac, end = '')

            # print tree characters
            char_current = char[cur_tree % tree_types]
            print(char_current * (cur_line * 2 + 1), end = '')

            # print ending spaces
            print((line_count-cur_line)*spac,end='')
        print('')

    # Print the trunk
    for cur_tree in range (0,tree_count):
        print((line_count - 1)* spac, end = '')
        char_current = char[cur_tree % tree_types]
        print(char_current, end = '')
        print((line_count)*spac, end='')

n = 2
m = 10
# tree_types = 1000

# interaktivny input
match len(sys.argv):
    # Fully interactive input (ask user for n and tree_count)
    case 1:
        print('n = ', end = '', file = sys.stderr)
        n = int(input())
        print("m = ", end = '', file = sys.stderr)
        m = int(input())
    # Use argument for n and user input for tree_count
    case 2:
        n = int(sys.argv[1])
        print("m = ", end = '', file = sys.stderr)
        m = int(input())
    # Use arguments for n and tree_count, ignore input
    case 3:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    case _:
        print("Invalid arguments", file = sys.stderr)
        # 0 means success, non 0 means error
        exit(1)

# Skusime spustit kod v 'try:'
# Ak tento kod vyhodi vynimku, spusti sa hned kod v 'except ex:'
# Po spusteni 'try:' (a aj pri pripadnom neuspechu a spusteni 'except ex:') sa
# spusti kod vo 'finally:'
"""
try:
    # Skusime spustit print_tree. Ak vyhodi vynimku, spusti sa kod v 'except ex:'
    print_tree(3, 5, 4)
except ex:
    # Kod na vyriesenie chyby (vynimky), ktora nastala v 'try:'
    print(ex)
finally:
    # Kod, ktory sa spusti po 'try:' a pripadnom 'except:'
    pass
"""

# print_tree(n, m, tree_types)
print_tree(n, m, len(char))


# Check if stdout is interactive

"""
if is_tty:
    print('n = ', end = '')
n = int(input())

if is_tty:
    print("tree_count = ", end = '')
tree_count = int(input())
"""
