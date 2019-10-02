#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:33:54 2019

@author: ali
"""
import numpy as np
import matplotlib.pyplot as plt



class Dragon:
    
    def __init__(self, arr):
        self.arr = arr
        self.arr_rot=0
        self.arr_tran=0
        self.arr_1=0
        self.arr_2=0
        self.temp = 0
        self.final_arr=0
        
    def rot1(self, th):
        rot_matrix = np.array([[np.cos(-th), np.sin(-th)],
                                [-np.sin(-th), np.cos(-th)]])
        i=0
        self.arr_1 = np.zeros(self.arr.shape)
        for raw in self.arr:
            
            self.arr_1[i] =  rot_matrix @ raw
            i+=1
        
    def rot2(self, th):
        rot_matrix = np.array([[np.cos(-th), np.sin(-th)],
                                [-np.sin(-th), np.cos(-th)]])
        self.arr_2 = np.zeros(self.arr.shape)
        i=0
        for raw in self.arr_tran:
            self.arr_2[i] = rot_matrix @ raw
            i+=1
            
        #self.arr_2 = self.arr_tran @ rot_matrix
        self.arr_2 = self.arr_2 + self.arr_1[-1]
    
    def origin_move(self):
        self.temp = np.zeros(self.arr_1.shape)
        i=1
        for raw in self.arr_1:
            self.temp[-i] = raw
            i+=1
            
        self.arr_tran = self.temp - self.temp[0]
       
        
    def end(self):
        self.final_arr = np.vstack((self.arr_1, self.arr_2))
        self.arr = self.final_arr
        
    def display(self):
        plt.plot(self.final_arr[:,0], self.final_arr[:,1])
        plt.axis('equal')
        
        
    
    
dragon = Dragon(np.array([[0,0],[1,0]]))
for i in range(6):
    dragon.rot1(-np.pi/4)
    dragon.origin_move()
    dragon.rot2(-np.pi/2)
    dragon.end()
    print(i)
    
    
    
dragon.display()


