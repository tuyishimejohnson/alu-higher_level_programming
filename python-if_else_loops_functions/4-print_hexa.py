#!/usr/bin/python3

print(*["{} = 0x{:x}".format(i, i) for i in range(99)], sep='\n')
