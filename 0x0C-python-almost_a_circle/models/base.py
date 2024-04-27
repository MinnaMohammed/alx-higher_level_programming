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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        '''
        A method that writes the JSON string represent. of list_objs to a file
        '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + '.json'
        # Construct a list of dicts representing each object's attributes
        obj_dicts = [obj.to_dictionary() for obj in list_objs]
        # Convert the list of dictionaries to a JSON string
        json_str = cls.to_json_string(obj_dicts)
        # Write the JSON string to the file
        with open(filename, mode='w') as file:
            file.write(json_str)
