#!/usr/bin/python3
''' Python Module '''
import json


class Base:
    ''' Base Class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Base Class Constructor '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' A method that returns the JSON string representation of a dict '''
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
