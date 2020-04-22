

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

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

pos = [(0,0)]

def init():
    line.set_data([0],[0])
    line2.set_data(t[-50], x[-50])
    line3.set_data([0],[0])
    return line, line2, line3


def animate(i):
    print(t[i])

    line.set_data(t[i], x[i])
    line2.set_data(t[-i],x[-i])
    line3.set_data([0], x[i])
    return line, line2, line3


anim = animation.FuncAnimation(fig, animate, init_func = init,frames=1000, interval=10, blit=True)
plt.show()
