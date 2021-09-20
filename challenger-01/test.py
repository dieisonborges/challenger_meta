#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chalenge1 import *

class IndexArrayTargetTest(unittest.TestCase):

    def test_index_0_1_target_9(self):
        self.assertEqual(index_array_target([2,7,11,15],9), (0,1))
        self.assertEqual(index_array_target([4,5,2,15],9), (0,1))
        self.assertEqual(index_array_target([8,1,2,10],9), (0,1))
        self.assertEqual(index_array_target([1,8,2,10],9), (0,1))
    
    def test_index_2_3_target_9(self):
        self.assertEqual(index_array_target([11,15,2,7],9), (2,3))
        self.assertEqual(index_array_target([122,15,4,5],9), (2,3))
        self.assertEqual(index_array_target([300,15,8,1],9), (2,3))
        self.assertEqual(index_array_target([2,15,6,3],9), (2,3))
    
    def test_index_0_1_target_5(self):
        self.assertEqual(index_array_target([2,3,2,7],5), (0,1))
        self.assertEqual(index_array_target([3,2,4,5],5), (0,1))
        self.assertEqual(index_array_target([0,5,8,1],5), (0,1))
        self.assertEqual(index_array_target([4,1,6,3],5), (0,1))
    
    def test_index_2_3_target_5(self):
        self.assertEqual(index_array_target([11,15,1,4],5), (2,3))
        self.assertEqual(index_array_target([14,16,2,3],5), (2,3))
        self.assertEqual(index_array_target([30,18,3,2],5), (2,3))
        self.assertEqual(index_array_target([21,15,0,5],5), (2,3))
    
    def test_index_0_4_target_2(self):
        self.assertEqual(index_array_target([1,15,3,1],2), (0,3))
        self.assertEqual(index_array_target([0,16,55,2],2), (0,3))
    
    def test_index_0_2_target_10(self):
        self.assertEqual(index_array_target([5,15,5,3],10), (0,2))
        self.assertEqual(index_array_target([8,16,2,2],10), (0,2))

if __name__ == "__main__":
    unittest.main()