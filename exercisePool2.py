#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 20:59:34 2022

@author: hasib
"""

### Exercise Pool 2 [Advanced Numpy]

import numpy as np
import sys

if sys.argv[1] == "ex1":
    y = np.random.randint(0, 4, size=20, dtype=(int))
    t = np.random.randint(0, 4, size=20, dtype=(int))
    ln = len(t)
    
    print('Output Value: ', y ,'\nTarget Value: ', t)
    confusion = np.zeros((4, 4))
        
    for i in range(ln):
        y_val = y[i]
        t_val = t[i]
        confusion[t_val][y_val] += 1
            
    tp = np.trace(confusion)
    total = np.sum(confusion)   
    confusion = confusion.astype(int)

    print('\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in confusion]))
    
    accuracy = tp/total
    print('\nModel Accuracy is: ' + str(accuracy*100))
    
if sys.argv[1] == "ex2":    
    y = np.arange(20, dtype=int)
    t = np.arange(20, dtype=int)
    ln = len(t)
    print('Output Value: ', y ,'\nTarget Value: ', t)
    p = np.random.permutation(ln)
    t, y = t[p], y[p]
    print('After Shuffle\nOutput Value: ', y ,'\nTarget Value: ', t)
    
if sys.argv[1] == "ex3":
    t = np.random.randint(0, 10, size=20, dtype=(int))
    nb_classes = 10
    one_hot_targets = np.eye(nb_classes)[t]
    one_hot_targets = one_hot_targets.astype(int)
    print('Target: ', t, '\nEncoded: \n', one_hot_targets)