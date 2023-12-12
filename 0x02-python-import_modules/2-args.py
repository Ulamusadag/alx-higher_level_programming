#!/usr/bin/python3

if __name__ == "__main__":
    num = len(sys.argv)
    if num == 1:
        print("{} argument:".format(num))
        print("{}: {}".format(num, sys.argv[1]))
    elif num == 0:
        print("{} arguments.".format(num))
    else:
        for i in sys.argv[1:]:
            j = 1
            print("{} arguments:".format(num))
            print("{}: {}".format(j, i))
            j += 1
