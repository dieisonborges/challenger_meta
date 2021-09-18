#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chalenge2 import *

class CheckBalancedBracketTest(unittest.TestCase):

    def test_bracket_SIM(self):
        self.assertEqual(check_balanced_bracket("{[()]}"), "SIM")     
        self.assertEqual(check_balanced_bracket("{{[[(())]]}}"), "SIM")
        self.assertEqual(check_balanced_bracket("(((({{{[[{{((()))}}]]}}}))))"), "SIM")        

    def test_bracket_NAO(self):
        self.assertEqual(check_balanced_bracket("{[)]}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[()]}{[()]}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[((((((((((}})))))))))])}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[ASD(])}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[(344])}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[(***])}"), "NAO")
        self.assertEqual(check_balanced_bracket("{[$$(])}"), "NAO")
       

if __name__ == "__main__":
    unittest.main()