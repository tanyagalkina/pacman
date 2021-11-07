#!/usr/bin/env python

import sys
import operator
from get_map import *

'''def display_help():
    print("USAGE:\n\t./304pacman file c1 c2")
    print("DESCRIPTION:\n\tfile\tfile describing the board, using the following characters:")
    print("\t\t    'O' for an empty square,")
    print("\t\t    '1' for a wall,")
    print("\t\t    'F' for the ghost's position,")
    print("\t\t    'P' for Pacman's position.")
    print("\tc1\tcharacter to display for a wall")
    print("\tc2\tcharacter to display for an empty space.")'''

def main_func(av):
    if len(av) == 2 and (av[1] == '-h' or av[1] == '--help'):
        display_help()
        return
    if len(av) is not 4:
        print('Wrong number of args, please try with -h ...', file=sys.stderr)
        sys.exit(84)
    map = get_map(av)
    for l in map:
        print (l)


if __name__ == '__main__':

    argv = sys.argv
    main_func(argv)

    sys.exit(0)
