#!/usr/bin/python3
'''
  Testing the Base model :)
'''

from models.base_model import BaseModel


'''class TestModel(BaseModel):
   
      The test model :)
    '''
j = BaseModel()
print()
print(j)
print()
print(j.id)
print('Created at', j.created_at)
print('Updated at', j.updated_at)
print()
print(j.to_dict())
print()
print()
l = BaseModel()
print(l)
print()
print(l.id)
print('Created at', l.created_at)
print('Updated at', l.updated_at)
print()
print(l.to_dict())
print()
print()
