#!/usr/bin/python3
def main(argv):
    argc = len(argv)
    ops = {
        '+': calculator_1.add,
        '-': calculator_1.sub,
        '*': calculator_1.mul,
        '/': calculator_1.div,
    }
    if argc != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op not in '+-*/':
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    res = ops[op](a, b)
    print('{:d} {:s} {:d} = {:d}'.format(a, op, b, res))

<<<<<<< HEAD

if __name__ == '__main__':
    from sys import argv, exit
    import calculator_1
    main(argv)
=======
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, ops[sys.argv[2]](a, b)))
>>>>>>> 6e44dbb810fa4c7a93710e8feb168ce647df93c4
