#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()   

    for element in my_list:
        if element not in unique_integers:
            unique_integers.add(element)    

    sum_of_unique_integers = sum(unique_integers)
    return sum_of_unique_integers
