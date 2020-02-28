'''

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

'''

import numpy as np
import matplotlib.pyplot as plt

Avogadro = 6.022e+23
Boltzmann = 1.3804e-23

#
# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████


def computeForces(mass, vels, temp, relax, dt):
    natoms, ndims = vels.shape
    sigma = np.sqrt(2*mass*temp*Boltzmann/(relax*dt))
    noise = np.random.randn(natoms, ndims) * sigma[np.newaxis].T
    force = -vels * mass[np.newaxis].T / relax + noise

    return force

def integrate(pos, vels, forces, mass, dt):
    pos += vels*dt
    vels += forces*dt/mass[np.newaxis].T

def wallHitCheck(pos, vels, box):
    ndims = len(box)
    for i in range(ndims):
        vels[(pos[:,i] <= box[i][0]) | (pos[:,i] >= box[i][1])] *= -1


def run(**args):
    natoms, mass, dt, relax = args['natoms'], args['mass'], args['dt'], args['relax']
    temp, nsteps, box = args['temp'], args['steps'], args['box']

    mass = np.ones(natoms) * mass/Avogadro
    ndims = len(box)
    pos = np.random.rand(natoms, ndims)
    vels = np.random.rand(natoms, ndims)

    for i in range(ndims):
        pos[:,i] = box[i][0] + (box[i][1] - box[i][0])*pos[:,i]

    #plt.plot(pos[:,0],pos[:,1],'o')
    #plt.show()

    step = 0
    output=[]
    while step <= nsteps:
        step+=1
        forces = computeForces(mass, vels, temp, relax, dt)
        integrate(pos, vels, forces, mass, dt)
        wallHitCheck(pos, vels, box)
        inst_temp = np.sum(np.dot(mass, (vels - vels.mean(axis=0))**2))/(3*Boltzmann*natoms)  # this come form the equpartition theorem. for D/2KbT = 1/2mV^2
        output.append([dt * step, inst_temp])


    return np.array(output)



'''

# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████

'''
if __name__ == "__main__":
    params = {
    'natoms':1000,
    'raduis':120e-12,
    'mass':1e-3,
    'dt':1e-15,
    'relax':10e-13,
    'temp':300,
    'steps':10000,
    'freq':100,
    'box':((0,10e-9),(0,10e-9),(0,10e-9)),
    'ofname':'traj_hydrogen.dump'
    }

    output = run(**params)
    plt.plot(output[:,0] * 1e12, output[:,1])
    plt.show()
