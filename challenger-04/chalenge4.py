#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
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
    map_max_lines = max(map)
    graph_map = ""
    first_block_lock = False    
    first_block = 0
    end_block = 0
    counter_water = 0

    #list lines of blocks
    for line in reversed(range(map_max_lines)):
        first_block_lock = False
        end_block_lock = False
        first_block = []
        end_block = []
        #list columns of blocks
        for column, value in enumerate(map) :
            if value>line:
                #Block                
                if(first_block_lock==False):
                    first_block=column
                    first_block_lock = True
                end_block = column  
        for column, value in enumerate(map) :
            if value>line:
                #Block
                end_block = column                 
        for column, value in enumerate(map) :
            if value>line:
                #Block                
                graph_map = graph_map + "\u25A0 "
                if(first_block_lock==False):
                    first_block=column
                    first_block_lock = True
            else:
                #Empty  
                if column>first_block and column<end_block:
                    graph_map = graph_map + "\u25A8 "
                    counter_water+=1
                else:
                    graph_map = graph_map + "\u25A1 "
        graph_map = graph_map + "\n"
    
    #Optional
    print(graph_map)
 
    return counter_water