import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

N = 5
L = 10
pos  = np.random.random((N,2))*L
vel = np.random.random((N,2))

table = np.vstack((pos,vel))


fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
	#table[:,1]+=table[:,3]
	table[:,0]+=table[:,2]
	line.set_data(table[:,0], table[:,1])
	return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html

plt.show()

