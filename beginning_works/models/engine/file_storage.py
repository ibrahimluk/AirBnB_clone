#!/usr/bin/python3
'''
  This is the File Storage module
  for AirBnB clone project :)
'''

import os
import json


class FileStorage:
    '''
      Serializes instances to a JSON file and
      Deserializes JSON file to instances :)
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
          Returns the __objects dictionary :) 
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
          Sets an obj with key <obj class name>.id in __objects
        '''
        key = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        '''
          Serializes __objects to the JSON file
          whose path is  __file_path ~ file.json  :)  
        '''
        print('\n  before storage.save\n')
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as l:
            print('\n  inside storage.save\n')
            j = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(j, l)
        print('\n  after storage.save\n')

    def reload(self):
        '''
          Deserializes a JSON file whose path,
          __file.json exits to __objects  :)
          This process restores the object that was stored :)
        '''
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, 'r', encoding='utf-8') as l:
            my_object = json.load(l)
            FileStorage.__objects = my_obejct
