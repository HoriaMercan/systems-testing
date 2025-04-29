import unittest
from node import Node
from tree import Tree

class TreeTest(unittest.TestCase):
    """ Test class for Tree """

    def setUp(self):
        """ Set up the test case """
        self.tree = Tree()
        self.tree.add(3)
        self.tree.add(4)
        self.tree.add(0)
        self.tree.add(8)
        self.tree.add(2)

    def test_add(self):
        """ Test the add method """
        node = self.tree.find(4)
        self.assertIsNotNone(node, "Node with value 4 should be found")
        self.assertEqual(node.data, 4, "Node data should be 4")

    def test_find(self):
        """ Test the find method """
        node = self.tree.find(5)
        self.assertIsNone(node, "Node with value 5 should not be found")
        
    def test_find1(self):
        """ Test the find method """
        node = self.tree.find(3)
        self.assertIsNotNone(node, "Node with value 3 should be found")
        self.assertEqual(node.data, 3, "Node data should be 3")        


        

if __name__ == "__main__":
    unittest.main()