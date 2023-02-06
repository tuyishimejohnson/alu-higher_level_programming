#!/usr/bin/python3

def uppercase(str):

    for i in range(len(str)):

        if ord(str[i]) >= 97 and ord(str[i]) <= 122:

            str = str[:i] + chr(ord(str[i]) - 32) + str[i+1:]

    print("{}\n".format(str), end="")
    

