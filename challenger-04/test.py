#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chalenge4 import *

class CheckProfitTest(unittest.TestCase):

    def test_water_retain(self):
        self.assertEqual(water_retain([0,1,0,2,1,0,1,3,2,1,2,1]), 6)   
        self.assertEqual(water_retain([0,5,0,2,1,0,1,8,2,1,2,1]), 22) 
        self.assertEqual(water_retain([0,1,0,2,1,0,1,3,2,1,2,1]), 6) 
        self.assertEqual(water_retain([0,10,0,2,1,0,1,30,2,1,2,1]), 47) 
        self.assertEqual(water_retain([0,1,0,2,10,0,1,3,2,10,2,1]), 35)   
        self.assertEqual(water_retain([5,4,3,2,1,2,3,4,5,6,7,8]), 16) 
        self.assertEqual(water_retain([100000,1,0,2,12312,0,1,3,123123,10,2,123123]), 933915) 
        self.assertEqual(water_retain([0,0,0,0,0,0,1,0,0,0,0,0]), 0) 
        self.assertEqual(water_retain([0,1,0,2]), 1) 
        self.assertEqual(water_retain([0,1]), 0) 

if __name__ == "__main__":
    unittest.main()