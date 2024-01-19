#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    k = len(argv) - 1
    if k < 1:
        print("{} arguments.".format(k))
    elif k == 1:
        print("{} argument:".format(k))
    else:
        print("{} arguments:".format(k))

    for i in range(k):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
