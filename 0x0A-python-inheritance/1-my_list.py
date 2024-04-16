#!/usr/bin/python3
'''MyList module'''


class MyList(list):
    '''MyList class

    Public instance method:
        def print_sorted(self): Prints the list sorted in ascending order.
    '''

    def print_sorted(self):
        '''A function that sorts a list'''
        return(sorted(self))
