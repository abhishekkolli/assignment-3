#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:37:56 2021

@author: kolliabhishek
"""

"""Caesar encryption and decryption"""

test1 = "Experience is the teacher of all things."
key1=12
alphabets = "abcdefghijklmnopqrstuvwxyz"

def movealphabets(string, key):
    newstr=""
    for i in range(len(string)):
        if key+i<len(string):
            newstr = newstr+string[key+i]
        else:
            newstr = newstr+string[key+i-len(string)]            
    return newstr
#test if the above is the right compuation or not print(movealphabets(alphabets, 5))


# test to decrypt message print(decipher_dict)

def encrypt(message, key):
    encrypted=""
    for i in message:
        if i.lower() in alphabets:
            if i.isupper():
                encrypted = encrypted + cipher_dict[i.lower()].upper()
            else:
                encrypted = encrypted + cipher_dict[i.lower()].lower()
        else:
            encrypted = encrypted + i
    return encrypted

def decrypt(message, key):
    decrypted=""
    for i in message:
        if i.lower() in alphabets:
            if i.isupper():
                decrypted = decrypted + decipher_dict[i.lower()].upper()
            else:
                decrypted = decrypted + decipher_dict[i.lower()].lower()
        else:
            decrypted = decrypted + i
    return decrypted

movedalphabets= movealphabets(alphabets, key1)
cipher_dict={}
for i in range(len(alphabets)):
    cipher_dict[alphabets[i]] = movedalphabets[i]

decipher_dict={}
for i,j in cipher_dict.items():
    decipher_dict[j] = i

print(encrypt(test1, key1))