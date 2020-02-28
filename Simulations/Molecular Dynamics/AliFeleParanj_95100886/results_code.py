

#  █████  ██      ██     ███████ ███████ ██      ███████     ██████   █████  ██████   █████  ███    ██      ██
# ██   ██ ██      ██     ██      ██      ██      ██          ██   ██ ██   ██ ██   ██ ██   ██ ████   ██      ██
# ███████ ██      ██     █████   █████   ██      █████       ██████  ███████ ██████  ███████ ██ ██  ██      ██
# ██   ██ ██      ██     ██      ██      ██      ██          ██      ██   ██ ██   ██ ██   ██ ██  ██ ██ ██   ██
# ██   ██ ███████ ██     ██      ███████ ███████ ███████     ██      ██   ██ ██   ██ ██   ██ ██   ████  █████

#  █████  ███████  ██  ██████   ██████   █████   █████   ██████
# ██   ██ ██      ███ ██  ████ ██  ████ ██   ██ ██   ██ ██
#  ██████ ███████  ██ ██ ██ ██ ██ ██ ██  █████   █████  ███████
#      ██      ██  ██ ████  ██ ████  ██ ██   ██ ██   ██ ██    ██
#  █████  ███████  ██  ██████   ██████   █████   █████   ██████


# ███    ███  ██████  ██      ███████  ██████ ██    ██ ██       █████  ██████
# ████  ████ ██    ██ ██      ██      ██      ██    ██ ██      ██   ██ ██   ██
# ██ ████ ██ ██    ██ ██      █████   ██      ██    ██ ██      ███████ ██████
# ██  ██  ██ ██    ██ ██      ██      ██      ██    ██ ██      ██   ██ ██   ██
# ██      ██  ██████  ███████ ███████  ██████  ██████  ███████ ██   ██ ██   ██

# ██████  ██    ██ ███    ██  █████  ███    ███ ██  ██████ ███████
# ██   ██  ██  ██  ████   ██ ██   ██ ████  ████ ██ ██      ██
# ██   ██   ████   ██ ██  ██ ███████ ██ ████ ██ ██ ██      ███████
# ██   ██    ██    ██  ██ ██ ██   ██ ██  ██  ██ ██ ██           ██
# ██████     ██    ██   ████ ██   ██ ██      ██ ██  ██████ ███████





import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML


def initval(ndim,box,natom):

    sigma = 1
    n = natom
    data_ = []
    x=-10
    dot_row = 5
    for row in range(dot_row):
        x += sigma
        y=-10
        for i in range(int(n/dot_row)):
            y += sigma
            data_.append([x,y])
    data_ = np.array(data_)

    data = np.ones((natom,int(2*ndim)))
    data[:,0] = box[0][0] + (box[0][1] - box[0][0])* np.random.random(natom)
    data[:,1] = box[1][0] + (box[1][1] - box[1][0])* np.random.random(natom)
    data[:,2] = (np.random.random(natom) * 2 - 1)*400
    data[:,3] = (np.random.random(natom) * 2 - 1)* 400
    data[:,2] -= np.mean(data[:,2])
    data[:,3] -= np.mean(data[:,3])

    for i in range(data_.shape[0]):
        data[i,0] = data_[i,0]
        data[i,1] = data_[i,1]

    return data



def periodic_wall():
    data[:,0][data[:,0] > box[0][1]] = box[0][0]
    data[:,0][data[:,0] < box[0][0]] = box[0][1]
    data[:,1][data[:,1] > box[1][1]] = box[1][0]
    data[:,1][data[:,1] < box[1][0]] = box[1][1]

def Force_cal_X(x1,x2,y1,y2):
    r2 = (x1-x2)**2 + (y1-y2)**2
    r6 = r2*r2*r2
    r12 = r6*r6
    F = 40*(12*sigma**12/(r12) - 6*sigma**6/(r6))*(x1-x2)/(r2)
    return F

def Force_cal_Y(x1,x2,y1,y2):
    r2 = (x1-x2)**2 + (y1-y2)**2
    r6 = r2*r2*r2
    r12 = r6*r6
    F = 40*(12*sigma**12/(r12) - 6*sigma**6/(r6))*(y1-y2)/(r2)
    return F

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

def Pressure_calculator():
    Forces = force(data)
    #Forces = np.array(Forces)
    P = np.array(Forces[0]) * data[:,0] + np.array(Forces[1]) * data[:,1]
    P = np.sum(P)/100
    return P

def wall_hit():
    data[:,2][ (data[:,0] > box[0][1]) + (data[:,0] < box[0][0]) ] *= -1
    data[:,3][ (data[:,1] > box[1][1]) + (data[:,1] < box[1][0]) ] *= -1


def move():
    Forces_n = force(data)
    data[:,0] = data[:,0] + data[:,2]*dt + 0.5* Forces_n[0]*dt**2
    data[:,1] = data[:,1] + data[:,3]*dt + 0.5* Forces_n[1]*dt**2
    Forces_n1 = [-data[:,0], -data[:,1]]
    data[:,2] += 0.5*(Forces_n[0] + Forces_n1[0])*dt
    data[:,3] += 0.5*(Forces_n[1] + Forces_n1[1])*dt

def file_init():
    f = open('results.csv','+w')
    f.write('X\tY\tV_x\tV_y\n')
    return f

def file_write(data,f):
    f.write('%3.5f\t%3.5f\t%3.5f\t%3.5f\n'%(data[0],data[1],data[2],data[3]))
    return f

def file_close(f):
    f.close()


def Energy():
    U = 0
    K = 0
    for i in range(natom-1):
        X1 = data[i,0]
        Y1 = data[i,1]
        for j in range(i+1,natom):
            X2 = data[j,0]
            Y2 = data[j,1]
            r2 = (X1-X2)**2 + (Y1-Y2)**2
            r6 = r2*r2*r2
            r12 = r6*r6
            U+=40*(sigma**12/(r12) - sigma**6/(r6))
    for atom in range(natom):
        K += 1/2 * (m) * (data[atom,2]**2 + data[atom,3]**2)
    E = U + K
    return U,K,E


def right_particle_counter():
    numebr = len(data[data[:,0] > 0])
    return numebr

def temperature_calculator():
    T = 0
    T += np.sum(data[:,2]**2 + data[:,3]**2)
    T /= (2000*natom)
    return T

def vel_outocorellation(data_list):
    first = 0
    i=3
    second = 0
    third = 0
    vel1 = []
    vel2 = []
    corr = []
    for tau in range(1,int(T/2)):
        N = 0
        for t in range(int(T)-tau):
            N+=1
            first+=np.mean(data_list[t][:,i]*data_list[t+tau][:,i])
            second+=np.mean(data_list[t][:,i])
            third+=np.mean(data_list[t+tau][:,i])
            vel1.append(data_list[t][:,i])
            vel2.append(data_list[t+tau][:,i])
        first /= N
        second /= N
        third /= N
        result = (first - second*third)/(np.std(vel1)*np.std(vel2))
        corr.append((tau,-result+2))

    return corr




def main(**args):
    data_list = []
    #Energy_data = []
    #number_data = []
    #T_data = []
    #P_data  = []
    #f = open('results.csv','w+')
    #f.write('X\tY\tV_x\tV_y\n')
    for i in range(int(T)):
        data_list.append(data)
        #U,K,E = Energy()
        #number_data.append(right_particle_counter())
        #T_data.append(temperature_calculator())
        #P_data.append(Pressure_calculator())
        #Energy_data.append([U,K,E])
        #f.write('%3.5f\t%3.5f\t%3.5f\t%3.5f\n'%(data[1,0],data[1,1],data[1,2],data[1,3]))
        #f.write('hey')
        move()
        wall_hit()

    corr = vel_outocorellation(data_list)
    corr = np.array(corr)
    plt.plot(corr[:,0],corr[:,1])
    #f.close()
    #Energy_data = np.array(Energy_data)
    #number_data = np.array(number_data)
    #T_data = np.array(T_data)
    #plt.plot(T_data)
    #plt.plot(T_data, '8', ms= 0.8)
    #plt.plot(P_data)
    #plt.plot(P_data, '8', ms= 0.8)
    #plt.plot(number_data)
    #plt.plot(number_data, '8', ms = 0.7)
    plt.title('Velocity outocorrelation of Vy\nwith 50 atoms')
    #plt.plot(Energy_data[:,0],'o',label='Potential Energy',ms=2)
    #plt.plot(Energy_data[:,1],'o',label='Kinetik Energy ',ms=2)
    #plt.plot(Energy_data[:,2],'o',label='Total Energy',ms=2)
    plt.ylabel('corr')
    plt.xlabel('tau')
    #plt.ylim(0,100000)
    plt.legend()
    plt.show()







'''
# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████
'''
if __name__ == "__main__":
    sigma = 1
    params  ={
    "natom":70,
    "ndim":2,
    "box":[(-15*sigma,15*sigma),(-15*sigma,15*sigma)],
    "dt" : 0.0001,
    "sigma":1,
    "m" :1
    }

    natom, ndim, box, dt , sigma,m = params['natom'], params['ndim'], params['box'], params['dt'], params["sigma"], params['m']
    T = 200
    data = initval(params['ndim'],params['box'],params['natom'])




    main(**params)
