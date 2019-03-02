# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:30:08 2019

@author: 25806
"""

import os

path = "./source/cut_face/neg_small_2/"
dir = os.listdir(path)
fopen = open('./source/cut_face/bg1.txt', 'w')
for d in dir:
#    string = 'pos_small/' + d + ' 1 0 0 64 64' +'\n'
    string = 'neg_small_2/' + d +'\n'
    fopen.write(string)
fopen.close()