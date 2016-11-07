# -*- coding: utf-8 -*-
import os
import chgender

mcount = 0
fcount = 0
correct = 0


with open(os.getcwd() + '/female.txt', 'r') as f:
    for name in f:
    	name = name.strip('\n')
        fcount = fcount + 1
        if chgender.guess(name)[0] == 'female':
        	correct = correct + 1

with open(os.getcwd() + '/male.txt', 'r') as f:
    for name in f:
    	name = name.strip('\n')
        mcount = mcount + 1
        if chgender.guess(name)[0] == 'male':
        	correct = correct + 1
            
accuracy = 1. * correct/(fcount + mcount)
print('total male input: {} \ntotal female input: {} \naverage accuracy: {}' ''.format(mcount, fcount, accuracy))