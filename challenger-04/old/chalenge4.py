#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Chalenger 04 - Meta (Digital, Simple, Human)
Powered by: Dieison Borges in 16/09/2021 (dieison.com)
To test this code, use unittest, running:
$python3 -m unittest test.py
'''

def water_retain(map):
    '''
    Non-negative integer data representing a map of
    elevation where the width of each bar is 1, calculate how much
    water is able to retain after rain.
    '''
    line = ""
    for position, block in enumerate(map):
        print(block)
        if(block>0):
            #block
            line = line + "\u25A0 "
        else:
            #empty            
            if(position>1 and position<(len(map))):
                if((map[position-1]>0) and(map[position+1]>0)):
                    line = line + "\u25A8 "
                else:
                    line = line + "\u25A1 "
            else:
                    line = line + "\u25A1 "



    return line


print(water_retain([0,1,0,2,1,0,1,3,2,1,2,1]))