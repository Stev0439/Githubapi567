'''
Created on Mar 9, 2021

@author: Steven
'''
import unittest

from Gitrepos import gitrepo

class Test(unittest.TestCase):
    
    def test_richkempinski(self):
        self.assertEqual(len(gitrepo("richkempinski")),8,'there are 8 repos')
    def test_Stev0439(self):
        self.assertEqual(gitrepo("Stev0439")["567Trangle"],9, "there are 9 commits")
        self.assertEqual(gitrepo("Stev0439")["helloworld"],3, "there are 3 commits")
        self.assertEqual(gitrepo("Stev0439")["Homework-3"],3, "there are 3 commits")
        self.assertEqual(gitrepo("Stev0439")["Triangle"],3, "there are 3 commits")


if __name__ == "__main__":
    
    unittest.main()
