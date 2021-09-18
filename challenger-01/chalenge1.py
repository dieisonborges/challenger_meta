#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Chalenger 01 - Meta (Digital, Simple, Human)
Powered by: Dieison Borges in 16/09/2021 (dieison.com)
To test this code, use unittest, running:
$python3 -m unittest test.py
'''

def index_array_target(numbers, target):

    '''
    Given an array of integers, return the indices of the 
    two numbers so they add up to a target specific. 
    '''

    for index, value in enumerate(numbers) :  
        for index2, value2 in enumerate(numbers) :
                if value+value2==target:
                    if(index!=index2):
                        return(index, index2)