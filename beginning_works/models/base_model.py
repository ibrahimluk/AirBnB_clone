#!/usr/bin/python3
'''
  The Base Class for this projecth :)
'''

import uuid
from models import storage
from datetime import datetime


class BaseModel:
    '''
      This is the Base Class from which all
      other classes in this project will inherit:)
    '''

    def __init__(self, *args, **kwargs):
        '''
          Initializes instance attributes :)
          Args:
              ~ *args: list of argumnents
              ~ **kwargs: dict of key/value pair arguments
        '''
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == 'created_at':
                    self.__dict__['created_at'] = datetime.strptime(
                            kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.__dict__['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
          returns a nicely printable string representation :)
        '''
        return f'[{type(self).__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        '''
          Updates the public instance attribute updated_at :)
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
          Returns a dictionary that contains all the key/value
          pairs of __dict__ of the instance :)
        '''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
