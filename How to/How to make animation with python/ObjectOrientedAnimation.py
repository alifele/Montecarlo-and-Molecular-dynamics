

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

class Animatiocls():

    def __init__(self,Lines_list, fig):
        L = len(Lines_list)

        self.Lines_list = [1] * L

        for i in range(L):
            self.Lines_list[i] = Lines_list[i]

        #self.line1 = line1
        #self.line2 = line2
        #self.line3 = line3
        self.fig = fig



    def init(self):
        self.Lines_list[0].set_data([0],[0])
        self.Lines_list[1].set_data(t[-50], x[-50])
        self.Lines_list[2].set_data([0],[0])
        return self.Lines_list


    def animate(self, i):
        print(t[i])

        self.Lines_list[0].set_data(t[i], x[i])
        self.Lines_list[1].set_data(t[-i],x[-i])
        self.Lines_list[2].set_data([0], x[i])
        return self.Lines_list

    def start_animation(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func = self.init,frames=100, interval=10, blit=True, repeat= False)
        plt.show()




t = np.linspace(-10,10,1000)
x = np.sin(t)


fig = plt.figure()
ax = fig.add_subplot(3,3,(1,8))
ax.set_xlim((-10,10))
ax.set_ylim((-2,2))
ax.plot(t,x)
line, = ax.plot(t[0],x[0],'ro')
line2,= ax.plot(t[-1],x[-1],'bs')

ax2 = fig.add_subplot(3,3,(3,9))
ax2.set_ylim((-2,2))
ax2.set_xlim((-0.5,0.5))
ax2.plot([],[])


ax2.get_shared_y_axes().join(ax, ax2)
ax2.set_yticklabels([])
line3, = ax2.plot([],[],'r*')

animobj = Animatiocls([line,line2,line3], fig)
animobj.start_animation()
