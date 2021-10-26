#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 00:49:36 2021

@author: kolliabhishek
"""

"""coordinate geometry"""
import math
def coordinate_dictionary(filename):
    f=open('{}.txt'.format(filename),'r')
#sample=open('./textfiles/common_words.txt','r')
    co_dict={}
    for line in f:
        newline = line.rstrip()
        cleanlist = newline.split(",")
        co_dict[cleanlist[0]] = [float(cleanlist[1]), float(cleanlist[2]), 
                                 float(cleanlist[3])]
    #print(co_dict)
    f.close()
    return co_dict
coordinate_dict=coordinate_dictionary("points")
"""closest point to origin"""
origin=[0,0,0]

def distance(point1, point2):
    distancesquare = (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 + (point1[2]-point2[2])**2
    distance = math.sqrt(distancesquare)
    return distance

#print(distance(coordinate_dict['point1'], origin))
dist_dict={}
for i in coordinate_dict.keys():
    dist_dict[i] = distance(coordinate_dict[i], origin)
minimum = min(dist_dict.values())
#print(minimum)
reverse_key_value={}
for i in dist_dict.keys():
    reverse_key_value[dist_dict[i]] = i
#print(reverse_key_value)
print("closest point to orgin: ", reverse_key_value[minimum])
#print(dist_dict)

"""........................................xxxxxxxxx.................."""
"""two closest points"""
number_of_coordinates = len(coordinate_dict)
#print(number_of_coordinates)
distance_pq={}
#done=['point1','point2','point3','point4']
visited=[]
for i in coordinate_dict.keys():
    #print(i)
    for j in coordinate_dict.keys():
        if i != j:
            if j not in visited:
                distance_pq[i+" and "+j]=distance(coordinate_dict[i], coordinate_dict[j])
    visited.append(i)

#print(distance_pq)
closest=min(distance_pq.values())
print(closest)
revers_dic={}
for i in distance_pq.keys():
    revers_dic[distance_pq[i]] = i
print("closest two points are: ", revers_dic[closest])





    
    