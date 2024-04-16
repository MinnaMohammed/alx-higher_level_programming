#!/usr/bin/python3

'''BaseGeometry module'''


class BaseGeometry:
    '''BaseGeometry class

    Public instance methods:
        def area(self): raises an Exception
        def integer_validator(self, name, value): validates value
    '''

    def area(self):
        '''A function that raises an exception'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validate the value

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
