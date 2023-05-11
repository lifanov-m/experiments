#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:53:16 2023

@author: user
"""

import math

'''
def factorial(x):   
    result = 1
    for i in range(2, x):
        result *= i        
    return result
'''
    
#x = [i for i in range(1000, 1001)]

x = 130

print('x = ', x)

y1 = float(math.factorial(x))
y2 = float(x**x)

#y1 = [factorial(i) for i in x]
#y2 = [i**i for i in x]
'''
for i in range(0, len(x)):
    print('x=', x[i], '\n', 'y1 = ', y1[i], '\n', 'y2 = ', y2[i], '\n\n\n')
'''

print('x=', x, '\n', 'y1 = ', y1, '\n', 'y2 = ', y2, '\n\n\n')


