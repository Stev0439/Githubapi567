'''
Created on Mar 9, 2021

@author: Steven
'''
import unittest

from Gitrepos import gitrepo

class Test(unittest.TestCase):
    
    def test_richkempinski(self):
        richrepos = []
        self.assertEqual(len(gitrepo("richkempinski")),8,'there are 8 repos')


if __name__ == "__main__":
    
    unittest.main()