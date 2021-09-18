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
    map_max_y = max(map)
    graph_map = ""
    water = 0

    for position_y in reversed(range(map_max_y)):
        for position_x, value in enumerate(map) :
            if value>position_y:
                #Block                
                print("position: \u25A0 ","x",position_x, "y",position_y, "water", water)
                graph_map = graph_map + "\u25A0 "
            else:
                #Empty
                print("position: \u25A1 ","x",position_x, "y",position_y, "water", water)
                graph_map = graph_map + "\u25A1 "
                print("anterior position: \u25A1 ","x",position_x-1, "y",position_y, "water", water)


                
        graph_map = graph_map + "\n"
                
    print("\u25A8 ")

    return graph_map

print(water_retain([0,1,0,2,1,0,1,3,2,1,2,1]))