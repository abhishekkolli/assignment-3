#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 21:54:53 2021

@author: kolliabhishek
"""

#"""program to convert temperature from fahrenheit to celsius"""
ftemp=input("Enter temperature in Fahrenheit:")
def fahtocel(f):
    try:
        return (int(f)-32)*5/9 #testing if the entered input is a whole number or not
    except ValueError:
        return "Please enter a positive, whole numeric temperature."
print(fahtocel(ftemp))
