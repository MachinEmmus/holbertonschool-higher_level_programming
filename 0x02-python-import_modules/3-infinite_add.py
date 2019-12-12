#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    if len(sys.argv) == 0:
        print("{:d}".format(add))
    else:
        for i in range(1, len(sys.argv)):
            add = add + int(sys.argv[i])
    print("{:d}".format(add))
