#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:38:50 2019

@author: ali
"""
import numpy as np
import matplotlib.pyplot as plt


class Fern:
    
    def __init__(self, arr):
        
        self.arr = arr
        self.data = []
        
    def rot1(self):
        M = np.array([[0, 0, 0],
                      [0, 0.16, 0],
                      [0,0,1]])
        self.arr = M @ self.arr
        
    def rot2(self):
        M = np.array([[0.84, 0.09, 0],
                      [-0.09, 0.84, 2.6],
                      [0,0,1]])
        self.arr = M @ self.arr
        
    def rot3(self):
        M = np.array([[0.1, -0.26, 0],
                      [0.23, 0.22, 1.6],
                      [0,0,1]])
        self.arr = M @ self.arr
        
    def rot4(self):
        M = np.array([[-0.02, 0.28, 0],
                      [0.22, 0.24, 0.84],
                      [0,0,1]])
        self.arr = M @ self.arr   
        
        
    def end(self): 
        
        self.data.append(self.arr)
    
arr = np.zeros((3,))
arr[2] =1

fern = Fern(arr)    
for i in range(1000000):
    rand = np.random.random()
    
    if rand>0 and rand<0.01:
        fern.rot1()
    elif rand>0.01 and rand<0.86:
        fern.rot2()
    elif rand>0.86 and rand<0.93:
        fern.rot3()
    else:
        fern.rot4()
    
    fern.end()
    
data = fern.data
data = np.array(data)
        
plt.plot(data[:,0], data[:,1], ',b')
plt.axis('equal')