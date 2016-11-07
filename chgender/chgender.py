#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

__all__ = ['guess']

class Guesser(object):

    def __init__(self):
    	self._build_lib()
        self._build_model()

    def _build_lib(self):
        with open(os.path.join(os.path.dirname(__file__),'chinese_name_lib.txt'), 'r') as f:  
            data = f.read()  
            self.chinese_name_lib = data.split()

    def _build_model(self):
        self.male_total = 0
        self.female_total = 0
        self.freq = {}

        with open(os.path.join(os.path.dirname(__file__),'pinyin_dataset.txt'), 'r') as f:
            for line in f:
            	line = line.strip('\n')
                pinyin, male, female = line.split()
                self.male_total += int(male)
                self.female_total += int(female)
                self.freq[pinyin] = (int(female), int(male))

        self.total = self.male_total + self.female_total

        for pinyin in self.freq:
            female, male = self.freq[pinyin]
            self.freq[pinyin] = (1. * female / self.female_total,
                               1. * male / self.male_total)

    def guess(self, name):
        name = name.lower()
        full_name  = name.split()
        first_name = full_name[0]
        first_word = ""
        second_word = ""
        i = len(first_name) + 1

        while(i >= 0):
            if first_name[:i] in self.chinese_name_lib:
                if i == len(first_name):
                    first_word = first_name[:i]
                    break
                elif first_name[i:] in self.chinese_name_lib:
				    first_word = first_name[:i]
				    second_word = first_name[i:]
				    break
            i = i - 1

        if first_word == second_word:
        	return ('female', 0.9)
        pf = self.prob_for_gender(first_word, 0) * (self.prob_for_gender(second_word, 0)**2.5)
        pm = self.prob_for_gender(first_word, 1) * (self.prob_for_gender(second_word, 1)**2.5)
        
        if pm > pf:
            return ('male', 1. * pm / (pm + pf))
        elif pm < pf:
            return ('female', 1. * pf / (pm + pf))
        else:
            return ('unknown', 0)

    def prob_for_gender(self, word, gender=0):
    	if word  == "":
    		return 1
        p = 1. * self.female_total / self.total \
            if gender == 0 \
            else 1. * self.male_total / self.total

        p *= self.freq.get(word, (0, 0))[gender]

        return p


guesser = Guesser()
def guess(name):
    return guesser.guess(name)
