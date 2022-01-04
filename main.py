#
# Copyright (c) 2022 Jean-Baptiste Lièvremont
#

import sys

from lib.hello import sayHello

def main(args):
    if len(args) < 2:
        print(f'Usage: {args[0]} <name>')
        sys.exit(1)
    sayHello(args[1])

if __name__ == '__main__':
    main(sys.argv)
