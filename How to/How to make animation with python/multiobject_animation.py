

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc

t = np.linspace(-10,10,1000)
x = np.sin(t)

fig, ax = plt.subplots()
ax.set_xlim((-10,10))
ax.set_ylim((-10,10))
ax.plot(t,x)
line, = ax.plot(t[0],x[0],'ro')
line2,= ax.plot(t[-1],x[-1],'bs')
pos = [(0,0)]

def init():
    line.set_data([0],[0])
    line2.set_data(t[-50], x[-50])
    return line, line2


def animate(i):
    print(t[i])

    line.set_data(t[i], x[i])
    line2.set_data(t[-i],x[-i])
    return line, line2


anim = animation.FuncAnimation(fig, animate, init_func = init,frames=1000, interval=10, blit=True)
plt.show()
