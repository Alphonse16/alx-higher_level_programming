#!/usr/bin/python3
<<<<<<< HEAD
import hidden_4
if __name__ == "__main__":
    for i in dir(hidden_4):
        if i[:2] != "__":
            print(i)
=======
if __name__ == "__main__":
    import sys
    import hidden_4
    for n in dir(hidden_4):
        if n[:2] != "__":
            print(n)
>>>>>>> 6e44dbb810fa4c7a93710e8feb168ce647df93c4
