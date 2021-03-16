'''
Created on Mar 9, 2021

@author: Steven
'''
import unittest
from unittest import mock
from Gitrepos import gitrepo

class Test(unittest.TestCase):
    @mock.patch('Gitrepos.gitrepo', return_value= [1,2,3,4,5,6,7,8,9])
    def test_richkempinski(self, mock_output):
        self.assertEqual(len(gitrepo("richkempinski")),9,'there are 9 repos')
    @mock.patch('Gitrepos.gitrepo', return_value= {'567Trangle': 11,'helloworld': 3,'Homework-3': 3,'Triangle': 3,} )
    def test_Stev0439(self, mock_output):
        self.assertEqual(gitrepo("Stev0439")["567Trangle"],11, "there are 11 commits")
        self.assertEqual(gitrepo("Stev0439")["helloworld"],3, "there are 3 commits")
        self.assertEqual(gitrepo("Stev0439")["Homework-3"],3, "there are 3 commits")
        self.assertEqual(gitrepo("Stev0439")["Triangle"],3, "there are 3 commits")


if __name__ == "__main__":
    
    unittest.main()
