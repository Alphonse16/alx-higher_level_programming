#!/usr/bin/python3
class Base:
    """Represent the base model of all
    classes in 0x0C project

    Attributes:
              __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise the a new base.

        Args:
             id :  The identity of the base
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

