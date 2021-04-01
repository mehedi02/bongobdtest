# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:19:10 2021

@author: Mehedi
"""

a = {
     "key1": 1,
     "key2": {
         "key3": 1,
         "key4": {
             "key5": 4,
             "key6": {
                 "key7": 6
                 }
             }
         }
     }

expected_output = {
    'key1': 1,
    'key2': 1,
    'key3': 2,
    'key4': 2,
    'key5': 3,
    'key6': 3,
    'key7': 4
    }

output_dictionary = {}

def print_depth(data, depth=1):
    
    # Write function body
    for i in data:
        val = data[i]
        if isinstance(val, dict):
            print("{} {}".format(i, depth))
            output_dictionary[i] = depth
            depth +=1
            print_depth(val, depth)
        else:
            print("{} {}".format(i, depth))
            output_dictionary[i] = depth
    return output_dictionary

output = print_depth(a)

import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(print_depth(a), expected_output)


if __name__ == '__main__':
    unittest.main()