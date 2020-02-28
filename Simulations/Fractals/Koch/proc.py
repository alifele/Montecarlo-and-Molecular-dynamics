import numpy as np
import matplotlib.pyplot as plt
from numpy import pi

def rotate(th):
        
        return np.array([[np.cos(-th), -np.sin(-th)],
                          [np.sin(-th), np.cos(-th)]])
        

class Koch:
    
    

    def __init__(self, arr):
        
        self.arr = arr
        self.x = np.array([])
        self.y = np.array([])
        self.x_ = 0
        self.y_ = 0
        
        
    def scale(self):
        self.main = self.arr/ 3
        self.arr = self.main
        
    def rot_trans(self, th, tran):
        rot = rotate(th)
        self.arr = self.main @ rot
        self.arr += tran
        
    def display(self):
        plt.plot(self.x_, self.y_)
        plt.axis('equal')
    
    def add(self):
        x = self.arr[0:,0]
        y = self.arr[0:,1]
        
        self.x = np.hstack(( self.x, x))
        self.y = np.hstack((self.y, y))
        
    
    def end(self):
        self.arr = np.hstack((self.x.reshape(-1,1), self.y.reshape(-1,1)))
        self.x_ = self.x
        self.y_ = self.y
        self.x = np.array([])
        self.y = np.array([])
   
frac = Koch(np.array([[0,0],[1,0]]))

for i in range(7):

   
    frac.scale()
    frac.add()
    frac.rot_trans(pi/3, np.array([1/3,0]))
    frac.add()
    frac.rot_trans(-pi/3, np.array([1/3+1/6,np.tan(pi/3)/6]))
    frac.add()
    frac.rot_trans(0, np.array([2/3, 0]))
    frac.add()
    frac.end()
    

frac.display()





