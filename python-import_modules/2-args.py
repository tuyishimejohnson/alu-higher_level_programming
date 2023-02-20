#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argc = len(sys.argv) - 1  #we substract 1 to move out script name
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
