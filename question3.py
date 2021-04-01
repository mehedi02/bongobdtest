# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 23:39:20 2021

@author: Mehedi
"""

class Node:
	def __init__(self, value):
		self.value = value
		self.right = None
		self.left = None

def findLCA(node, n1, n2):
	if node is None:
		return None

	if node.value == n1 or node.value == n2:
		return node

	left_lca = findLCA(node.left, n1, n2)
	right_lca = findLCA(node.right, n1, n2)

	if left_lca and right_lca:
		return node

	return left_lca if left_lca is not None else right_lca

tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.left.left.left = Node(8)
tree.left.left.right = Node(9)

tree.right.right = Node(7)
tree.right.left = Node(6)



import unittest

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertEqual(findLCA(tree, 6,7).value, 3)
        self.assertEqual(findLCA(tree, 3,7).value, 3)
        self.assertEqual(findLCA(tree, 6,3).value, 3)
        self.assertEqual(findLCA(tree, 8,9).value, 4)
        self.assertEqual(findLCA(tree, 2,3).value, 1)
        self.assertEqual(findLCA(tree, 5,2).value, 2)
        self.assertEqual(findLCA(tree, 4,5).value, 2)


if __name__ == '__main__':
    unittest.main()







