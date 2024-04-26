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
        return self.width

    @size.setter
    def size(self, value):
        ''' size attr setter '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' A method that assigns attributes '''
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''String representation of Square instance.'''
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        ''' A method that returns a dictionary representation '''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
