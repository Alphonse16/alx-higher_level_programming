#!/usr/bin/python3
"""A rectangle class that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """
     Represents a Rectangle and
     Inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise a new rectangle.

        Args:
            width (int): The width of a new Rectangle.
            height (int): The height of a new Rectangle.
            x (int): The x coordinate 
            y (int): The y coordinate
            id (int): The identity of the new Rectangle

        Raises:
             TypeError: If either width or height is not an int.
             ValueError: If the width or height is <= 0.
             TypeError: If x or y are not int.
             ValueError: If x or y <0.             

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)


        @property
        def width(self):
            """set or get the width of a rectangle"""
            return self.width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError ("width must be an integer")
            if value <= 0:
                raise ValueError ("width must be > 0")
            self.__width = value


        @property
        def height(self):
            """set the height of a recatngle"""
            return self.height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError ("height must be an interger")
            if value <= 0:
                raise ValuError ("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """set x coordinate of a rectangle"""
            return self.x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError ("x must be an integer")
            if value < 0:
                raise ValueError ("x must be >= 0")
            self.__x = value


        @property
        def y(self):
            """set y coordinate of a rectangle"""
            return self.y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError ("y must be an integer")
            if value < 0:
                raise ValueError ("y must be >= 0")
            self.__y = value



