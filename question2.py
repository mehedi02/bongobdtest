# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:29:24 2021

@author: Mehedi
"""

class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)

a = {
     "key1": 1,
     "key2": {
         "key3": 1,
         "key4": {
             "key5": 4,
             "user": person_b
             }
         }
     }


expected_output = {
    'key1': 1,
    'key2': 1,
    'key3': 2,
    'key4': 2,
    'key5': 3,
    'user': 3,
    'self.first_name': 4,
    'self.last_name': 4,
    'self.father': 4,
    'self.first_name': 5,
    'self.last_name': 5,
    'self.father': 5
    }


output_dict = {}


def object_depth(data, depth):
    print("{} {}".format("self.first_name", depth))
    print("{} {}".format("self.last_name", depth))
    output_dict["self.first_name"] = depth
    output_dict["self.last_name"] = depth
    if data.father != None:
        print("{} {}".format("self.father", depth))
        output_dict["self.father"] = depth
        depth += 1
        object_depth(data.father, depth)
    else:
        print("{} {}".format("self.father", depth))
        output_dict["self.father"] = depth
        


# depth = 1
      
def print_depth(data, depth=1):
    
    # Write function body

    for i in data:
        val = data[i]
        if isinstance(val, dict):
            print("{} {}".format(i, depth))
            output_dict[i] = depth
            depth +=1
            print_depth(val, depth)
        elif hasattr(val, 'first_name'):
            print("{} {}".format(i, depth))
            output_dict[i] = depth
            depth += 1
            object_depth(val, depth)
        else:
            print("{} {}".format(i, depth))
            output_dict[i] = depth
    return output_dict
        

output = print_depth(a)

import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(print_depth(a), expected_output)


if __name__ == '__main__':
    unittest.main()