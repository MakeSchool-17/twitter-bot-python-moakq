import sys
from random import shuffle


def shuffle_arguments(arguments):
    shuffle(arguments)
    print(arguments)

if __name__ == '__main__':
    shuffle_arguments(sys.argv[1:])
