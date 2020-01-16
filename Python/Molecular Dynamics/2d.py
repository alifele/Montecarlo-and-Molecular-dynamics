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
    data[:,2] = (np.random.random(natom) * 2 - 1)*0.4
    data[:,3] = (np.random.random(natom) * 2 - 1)*0.4
    return data

def showinit(data,box):
    fig, ax = plt.subplots()
    ax.set_xlim((box[0][0]*1.1,box[0][1]*1.1))
    ax.set_ylim((box[1][0]*1.1,box[1][1]*1.1))
    line, = ax.plot(data[:,0], data[:,1],'o')

    return fig, ax, line

def init():
    line.set_data(data[:,0],data[:,1])
    return line,

def Animate():
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 100, interval=40, blit = True)
    plt.show()

def move():
    Forces_n = force(data)
    data[:,0] = data[:,0] + data[:,2]*dt + 0.5* Forces_n[0]*dt**2
    data[:,1] = data[:,1] + data[:,3] + 0.5* Forces_n[1]
    Forces_n1 = [-data[:,0], -data[:,1]]
    data[:,2] += 0.5*(Forces_n[0] + Forces_n1[0])
    data[:,3] += 0.5*(Forces_n[1] + Forces_n1[1])*dt


def wall_hit():
    data[:,2][ (data[:,0] > box[0][1]) + (data[:,0] < box[0][0]) ] *= -1
    data[:,3][ (data[:,1] > box[1][1]) + (data[:,1] < box[1][0]) ] *= -1

def periodic_wall():
    data[:,0][data[:,0] > box[0][1]] = box[0][0]
    data[:,0][data[:,0] < box[0][0]] = box[0][1]
    data[:,1][data[:,1] > box[1][1]] = box[1][0]
    data[:,1][data[:,1] < box[1][0]] = box[1][1]

def Force_cal_X(x1,x2,y1,y2):
    U = (x1-x2) / ((x1-x2)**2 + (y1-y2)**2)
    return U

def Force_cal_Y(x1,x2,y1,y2):
    U =  (y1-y2) / ((x1-x2)**2 + (y1-y2)**2)
    return U

def force(data):
    force_x= np.zeros((natom, natom))
    force_y= np.zeros((natom, natom))
    for particle in range(natom):
        x1, y1 = data[particle,0], data[particle,1]
        for front_particle in range(particle + 1, natom):
            x2, y2 = data[front_particle,0], data[front_particle,1]
            force_x[particle, front_particle] = Force_cal_X(x1,x2,y1,y2)
            force_x[front_particle, particle] = -force_x[particle, front_particle]
            F_X = np.sum(force_x, axis=1)
            force_y[particle, front_particle] = Force_cal_Y(x1,x2,y1,y2)
            force_y[front_particle, particle] = -force_y[particle, front_particle]
            F_Y = np.sum(force_y, axis=1)
            Forces  = [F_X, F_Y]


    return Forces







def animate(i):
    move()
    #wall_hit()
    periodic_wall()
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
    "box":[(-100,100),(-100,100)],
    "dt" : 0.001
    }
    natom, ndim, box, dt = params['natom'], params['ndim'], params['box'], params['dt']
    data = initval(params['ndim'],params['box'],params['natom'])
    fig, ax, line = showinit(data, params['box'])
    main(**params)
