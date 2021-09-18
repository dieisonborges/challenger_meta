#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Chalenger 03 - Meta (Digital, Simple, Human)
Powered by: Dieison Borges in 16/09/2021 (dieison.com)
To test this code, use unittest, running:
$python3 -m unittest test.py
'''

def check_profit(stocks):

    '''
    Let's say you have an array for which the element i
    is the price of a given share on day i.
    If you were allowed to complete at most one
    transaction (ie buy one and sell one share), create
    an algorithm to find the maximum profit.
    Note that you cannot sell a share before
    purchase.
    '''
   
    #Initiate Variables
    buy_day=0
    buy_stock_value=0    
    sell_day=0
    sell_stock_value=0
    profit=0

    for day, stock_value in enumerate(stocks) :        
        for day2, stock_value2 in enumerate(stocks) :
            if day!=day2:
                if (stock_value - stock_value2) > profit:                    
                    if day2<day:
                        buy_stock_value = stock_value2
                        buy_day = day2
                        sell_stock_value = stock_value                    
                        sell_day = day
                        profit = stock_value - stock_value2

    if(profit>0):
        return (
            "{} (Comprou no dia {} (preço igual a {}) e vendeu no dia {} (preço igual a {}), lucro foi de {} - {} = {}".format(
                profit,
                buy_day+1,
                buy_stock_value,
                sell_day+1,
                sell_stock_value,            
                sell_stock_value,
                buy_stock_value,
                profit
            )   
        )
    else:
        return "0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)"
    