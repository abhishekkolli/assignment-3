#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 02:46:56 2021

@author: kolliabhishek
"""
"apple"'apple'
f=open('speech.txt','r')
#for line in f:
#    line.strip("\n")
entirefile = f.read()
f.close()
entirefile = entirefile.replace('\n', ' ')
entirefile = entirefile.replace('.', ' ')
entirefile = entirefile.replace(',', ' ')
entirefile = entirefile.replace('"', ' ')
entirefile = entirefile.replace('” ', ' ')
entirefile = entirefile.replace("'", '')
entirefile = entirefile.replace("’", '')
entirefile = entirefile.replace('!', ' ')
for char in entirefile:
    if char in {',','.','!','\n','"','"',"'","'"}:
        entirefile.replace(char, ' ')
entirefile = entirefile.lower()
#print(entirefile.split())
speech_list=entirefile.split()
frequency={}
for i in speech_list:
    if i not in frequency.keys():
        frequency[i] = 1
    else:
        frequency[i]+=1
#print(frequency)
c=open('common_words.txt','r')
entiredfile = c.read()
entiredfile = entiredfile.lower()
cleanlist = entiredfile.split()
commonwords = sorted(cleanlist)
c.close()
#print(sortedlist)
for i in frequency.keys():
    if i in commonwords:
        frequency[i] = 0
#print(frequency)
used_words_frequency = sorted(frequency.values(), reverse=True)[0:20]
set_words = set(used_words_frequency)
used_words = sorted(list(set_words),reverse=True)
#print(used_words)
copy = 0
f1 = open("words.txt", "w")
for i in used_words:
    for j in frequency.keys():
        if frequency[j] == i and copy<=20:
            copy += 1
#            print(j,frequency[j])
              # append mode
            f1.write(str(j) + ' - '+str(frequency[j]) + "\n")
f1.close()

