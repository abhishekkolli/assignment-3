#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 02:16:42 2021

@author: kolliabhishek
"""

"""centered average"""
"""using set data structure it is easier since it vomits duplicates"""
def centered_average(array):
    if len(array)<3:
        return "enter atleast three numbers for computing centerd average"
    else:
        maximum = max(array)
        minimum = min(array)
        trim_list = [maximum,minimum]
        for i in array:
            if i not in [maximum,minimum]:
                trim_list.append(i)
        sum = 0
        j = 0
        for i in trim_list:
            j = j + 1
            sum = sum + i
        cen_ave = (sum - maximum - minimum)/(j-2)
    return cen_ave
lis = [1,1,1,2,2,3,4,5,6,8,6,7,9,9]
print(round(centered_average(lis),3))
                
def centered_averagenoiter(array):
    if len(array)<3:
        return "enter atleast three numbers for computing centerd average"
    else:
        maximum = max(array)
        minimum = min(array)
        trim_list = [maximum,minimum]
        for i in array:
            if i not in [maximum,minimum]:
                trim_list.append(i)
        num = sum(trim_list) - maximum - minimum
        den = len(trim_list) - 2
        cen_ave = num/den
    return cen_ave
print(round(centered_averagenoiter(lis),3))
                
                