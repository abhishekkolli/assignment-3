#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 19:07:28 2021

@author: kolliabhishek
"""

Input_number=input("Enter your input: ")
def Is_number(f):
    try:
        if float(f): #testing if the entered input is a whole number or not
            return True
    except ValueError:
        return False
print(Is_number(Input_number))