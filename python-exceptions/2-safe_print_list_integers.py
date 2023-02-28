#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end=' ')
                count += 1
        except IndexError:
            raise ValueError("x exceeds the length of my_list")
    print()
    return count
