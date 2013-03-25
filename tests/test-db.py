#!/usr/bin/env python
# coding: utf-8
import sys
sys.path.append("/Users/okamuuu/project/hello/app/lib")
import types
import unittest
import db

class TestDb(unittest.TestCase):
    
    def test_db(self):
      
        id = db.save({'url':'https://github.com/okamuuu'})
        print(id)
        url = db.find_one({'url':'https://github.com/okamuuu'})
        print(url)
        self.assertTrue(url)
 
if __name__ == "__main__":
    unittest.main()

