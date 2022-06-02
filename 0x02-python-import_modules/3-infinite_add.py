#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
<<<<<<< HEAD
    n = 0
    for i in range(len(argv) - 1):
        n += int(argv[i + 1])
    print("{:d}".format(n))
=======
    import sys
    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
>>>>>>> 6e44dbb810fa4c7a93710e8feb168ce647df93c4
