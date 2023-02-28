#!/usr/bin/python3
def safe_print_list(my_list=[],x=0):
    printed = 0
    try:
        while printed < x:
            print(my_list[printed], end="")
            printed += 1
    except IndexError:
        pass
    print("")
    return printed
