import sys


def reverse_arguments(arguments):
    reversed_arguments = arguments[::-1]
    for i in range(len(reversed_arguments)):
        reversed_arguments[i] = reversed_arguments[i][::-1]
    return reversed_arguments

if __name__ == '__main__':
    reversed = reverse_arguments(sys.argv[1:])
    print(" ".join(reversed))
