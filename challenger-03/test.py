#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from chalenge3 import *

class CheckProfitTest(unittest.TestCase):

    def test_stock_yes_transaction(self):
        self.assertEqual(
            check_profit([7,1,5,3,6,4]), 
            "5 (Comprou no dia 2 (preço igual a 1) e vendeu no dia 5 (preço igual a 6), lucro foi de 6 - 1 = 5"
            )
        self.assertEqual(
            check_profit([8,2,6,4,7,5]), 
            "5 (Comprou no dia 2 (preço igual a 2) e vendeu no dia 5 (preço igual a 7), lucro foi de 7 - 2 = 5"
            )
        self.assertEqual(
            check_profit([10,2,62,4,3,0]), 
            "60 (Comprou no dia 2 (preço igual a 2) e vendeu no dia 3 (preço igual a 62), lucro foi de 62 - 2 = 60"
            )
        self.assertEqual(
            check_profit([37,56,65,74,83,999999999991]), 
            "999999999954 (Comprou no dia 1 (preço igual a 37) e vendeu no dia 6 (preço igual a 999999999991), lucro foi de 999999999991 - 37 = 999999999954"
            )
        self.assertEqual(
            check_profit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), 
            "19 (Comprou no dia 1 (preço igual a 1) e vendeu no dia 20 (preço igual a 20), lucro foi de 20 - 1 = 19"
            )          
    
    def test_stock_no_transaction(self):
        self.assertEqual(
            check_profit([7,6,5,4,3,1]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
        self.assertEqual(
            check_profit([70,60,50,40,30,10]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
        self.assertEqual(
            check_profit([370,56,5,0,0,0]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
        self.assertEqual(
            check_profit([2,2,2,2,2,2]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
        self.assertEqual(
            check_profit([5,4,3,2,1,0]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
        self.assertEqual(
            check_profit([100,90,80,70,60,50,40,30,20,10,0]), 
            "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
            )
       

if __name__ == "__main__":
    unittest.main()