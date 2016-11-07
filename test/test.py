# -*- coding: utf-8 -*-
import os
import chgender

male = 0
female = 0
i = 0

with open(os.getcwd() + '/female.txt', 'r') as f:
    for name in f:
    	name = name.strip('\n')
    	i = i + 1
        if chgender.guess(name) == 0:
        	female = female + 1

with open(os.getcwd() + '/male.txt', 'r') as f:
    for name in f:
    	name = name.strip('\n')
    	i = i + 1
        if chgender.guess(name) == 1:
        	male = male + 1
            
result = 1. * (female + male)/i
print("accuracy: ")
print(result)