import numpy as np
import matplotlib.pyplot as plt


sigma = 1
natom = 25
n = natom
data_ = []
x=-12
y = 1
for row in range(int(natom**0.5)):
    x += sigma
    y=3
    for i in range(int(natom**0.5)):
        y += sigma
        data_.append([x,y])

data = np.array(data_)
plt.plot(data[:,0], data[:,1],'8')
plt.title('Box\nsigma=1')
plt.xlim([-15,15])
plt.ylim([-15,15])
plt.show()
