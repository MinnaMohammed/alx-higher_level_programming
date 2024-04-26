#!/usr/bin/python3
''' Python Module '''
from models.base import Base


class Rectangle(Base):
    ''' Rectangle Class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Rectangle Class Constructor '''
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Getter for the width attr'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter for width attr'''
        self.__width = value

    @property
    def height(self):
        '''Getter for height attr'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height attr'''
        self.__height = value

    @property
    def x(self):
        '''Getter for the x attr'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x attr'''
        self.__x = value

    @property
    def y(self):
        '''Getter for y attr'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y attr'''
        self.__y = value
