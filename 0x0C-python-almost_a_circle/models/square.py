#!/usr/bin/python3
''' Python Modules '''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square Class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Square Class Constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size attr getter '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' size attr setter '''
        self.__size = value

    def __str__(self):
        '''String representation of Square instance.'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
