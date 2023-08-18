# -*- coding: utf-8 -*-
"""
Created on Sun May 28 00:34:05 2023

@author: harry
"""

#random password generator
import random

passwordLength = int(input('What length password is required? (enter integer)'))
i = 0
character_list = []
password = ''

while i < passwordLength:
    character = random.randint(33, 128)
    character_list.append(chr(character))
    i += 1
    
for i, chr in enumerate(character_list):
    password += chr
    
print('your password is: \n' + password)