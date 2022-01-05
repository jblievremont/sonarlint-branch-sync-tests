#
# Copyright (c) 2022 Jean-Baptiste Lièvremont
#

import sys

from lib.hello import say_hello

def main(args):
    i = 0
    if len(args) < 2:
        print(f'Usage: {args[0]} <name>')
        sys.exit(1)
    say_hello(args[1])

if __name__ == '__main__':
    main(sys.argv)
