import numpy as np
import matplotlib.pyplot as plt

Avogadro = 6.022e+23
Boltzmann = 1.3804e-23


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

    setp = 0
    output=[]
    while step < nsteps:

        forces = computeForces(mass, vels, temp, relax, dt)
        pos, vels = integrate(pos.copy(), vels.copy(), forces, mass, dt)
        wallHitCheck(pos, vels, box)

        step+=1

if __name__ == "__main__":
    params = {
    'natoms':1000,
    'raduis':120e-12,
    'mass':1e-3,
    'dt':1e-15,
    'relax':10e-13,
    'temp':300,
    'steps':1000,
    'freq':100,
    'box':((0,10e-9),(0,10e-9),(0,10e-9)),
    'ofname':'traj_hydrogen.dump'
    }

    output = run(**params)
