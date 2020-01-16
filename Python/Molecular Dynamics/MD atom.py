import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
#
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████

def initval(ndim,box,natom):
    data = np.ones((natom,int(2*ndim)))
    data[:,0] = box[0][0] + (box[0][1] - box[0][0])* np.random.random(natom)
    data[:,1] = box[1][0] + (box[1][1] - box[1][0])* np.random.random(natom)
    data[:,2] = np.random.random(natom) * 2 - 1
    data[:,3] = np.random.random(natom) * 2 - 1
    return data

def showinit(data,box):
    fig, ax = plt.subplots()
    ax.set_xlim((box[0][0],box[0][1]))
    ax.set_ylim((box[1][0],box[1][1]))
    line, = ax.plot(data[:,0], data[:,1],'o')

    return fig, ax, line

def init():
    line.set_data(data[:,0],data[:,1])
    return line,

def Animate():
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 100, interval=30, blit = True)
    plt.show()

def move():
    data[:,0] += data[:,2]
    data[:,1] += data[:,3]

def wall_hit():
    data[:,2][ (data[:,0] > box[0][1]) + (data[:,0] < box[0][0]) ] *= -1
    data[:,3][ (data[:,1] > box[1][1]) + (data[:,1] < box[1][0]) ] *= -1



def animate(i):
    move()
    wall_hit()
    line.set_data(data[:,0],data[:,1])
    return line,


def main(**args):
    Animate()




'''
# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████
'''
if __name__ == "__main__":

    params  ={
    "natom":20,
    "ndim":2,
    "box":[(-10,10),(-10,10)]
    }
    natom, ndim, box = params['natom'], params['ndim'], params['box']
    data = initval(params['ndim'],params['box'],params['natom'])
    fig, ax, line = showinit(data, params['box'])
    main(**params)
