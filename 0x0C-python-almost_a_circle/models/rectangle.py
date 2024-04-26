#!/usr/bin/python3
''' Python Module '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle Class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Rectangle Class Constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Getter for the width attr'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width attr'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Getter for height attr'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height attr'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Getter for the x attr'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x attr'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Getter for y attr'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y attr'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' A method that calculates the area of a rectangle '''
        return self.width * self.height

    def display(self):
        ''' A method that prints the Rectangle with the character # '''
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        ''' String representation of Rectangle instance '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
