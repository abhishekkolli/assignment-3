#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:43:16 2021

@author: kolliabhishek
"""
def processfile(filename):
    try:
        f=open('{}.txt'.format(filename),'r')
#sample=open('./textfiles/common_words.txt','r')
        entirefile = f.read()
        entirefile = entirefile.lower()
    #print(entirefile)
    #print(type(entirefile))
        lines = 1
        for i in entirefile:
            if i == "\n":
                lines+=1
                #print(lines)
        cleanlist = entirefile.split()
    #print(len(cleanlist))
        sortedlist = sorted(cleanlist)
        f.close()
        return filename, sortedlist, lines
    except IOError:
        print("file doesn't exist")

(filename, items, lines)=processfile('common_words')
print((filename, items, lines))