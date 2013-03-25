#!/usr/bin/env python
# coding: utf-8
import sys
sys.path.append("./app/lib")
import types
import unittest
import base62

class TestBase62(unittest.TestCase):
    
    def test_base_decode(self):
       
        integer = base62.base62_decode('3d7');
        print(integer)
        self.assertTrue(integer)
 
    def test_base_encode(self):
       
        string = base62.base62_encode(12345);
        print(string)
        self.assertTrue(string)
        """ self.assertEqual(string, '')
        """
    
if __name__ == "__main__":
    unittest.main()

