#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
<<<<<<< HEAD
        return c
    else:
        return sub(a, b)
=======
        return (c)

    else:
        return(sub(a, b))
>>>>>>> 6e44dbb810fa4c7a93710e8feb168ce647df93c4
