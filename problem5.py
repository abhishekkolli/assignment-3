#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 23:32:29 2021

@author: kolliabhishek
"""

message="mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"
#message="ar"
#message = "qjbqduqzoq ue ftq fqmotqd ar mxx ftuzse"
"""how many keys are possible in total 26 alphabets so 26 keys. Going by this 
logic lets check for every key find out the message and see if any of the words
 in the message are in the common words list. probable assumption I am making is
 when I find the first match in common words I am exiting and printing the message"""

alphabets="abcdefghijklmnopqrstuvwxyz"
alpha_num = {}
num_alpha = {}
for i in range(len(alphabets)):
    alpha_num[alphabets[i]] = i
for j in range(len(alphabets)):
    num_alpha[j] = alphabets[j]
#print(alpha_num,num_alpha)

def match_dict(char, key):
    newchar=""
    indix = alpha_num[char] - key
    if indix >= 0:
        newchar = num_alpha[indix]
    else:
        newchar = num_alpha[len(alphabets)+indix]
    return newchar

def sortedlist(filename):
    f=open('{}.txt'.format(filename),'r')
#sample=open('./textfiles/common_words.txt','r')
    entirefile = f.read()
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
    return sortedlist
common_words=sortedlist('common_words')

def decrypted(message,key):
    newmessage=""
    for char in message:
        if char in alphabets:
            newmessage = newmessage + match_dict(char,key)
        else:
            newmessage = newmessage + char
    return newmessage

def decrypt(message):
    #messagelist = message.split()
    for i in range(1,len(alphabets)+1):
        key = i
        decrypted_message=decrypted(message,key)
        decryptlist = decrypted_message.split()
        for i in decryptlist:
            if i in common_words:
                #return True
                return key, decrypted_message

print(decrypt(message))

        









