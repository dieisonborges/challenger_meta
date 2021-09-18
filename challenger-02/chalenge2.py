#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Chalenger 02 - Meta (Digital, Simple, Human)
Powered by: Dieison Borges in 16/09/2021 (dieison.com)
To test this code, use unittest, running:
$python3 -m unittest test.py
'''

def check_balanced_bracket(brakets):

    '''
    A bracket is considered to be any one of the following characters: (, ), {, }, [ or ].
    Two brackets are considered a matched pair if the aperture bracket (this
    is, (, [or {) occurs to the left of a closing bracket (ie,),] or} of the
    exact same type. There are three types of bracket pairs: [ ], { } and ( ). EXAMPLE
    A matching bracket pair is not balanced if the aperture and the {[()]} YES
    {[(])} NO
    {{[[(())]]}} YES
    closing do not match each other. For example, { [ ( ] ) } is not balanced
    because the content between {and} is not balanced. The first bracket includes the
    opening, (, and the second includes an unbalanced closing bracket,].
    Given strings of characters, determine if each string of brackets is
    balanced. If a string is balanced, return YES. otherwise, return
    NO.
    '''

    #Check if it's even
    if (len(brakets) % 2) != 0:
        return "NAO"

    else:
        #Separates into two groups
        limit_group = int(len(brakets)/2)        
        brakets_group1 = brakets[0:limit_group]
        brakets_group2 = brakets[limit_group:len(brakets)]

        #Replace characters for comparison
        brakets_group2 = brakets_group2.replace(")", "(")
        brakets_group2 = brakets_group2.replace("}", "{")
        brakets_group2 = brakets_group2.replace("]", "[")

        #Check
        if(brakets_group1==brakets_group2[::-1]):
            return "SIM"
        else:
            return "NAO"