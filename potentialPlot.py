import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from random import shuffle


filename = 'output.pop'

def loadData(filename):
    raw = [map(float,l.strip().split()) for l in open(filename)]
    x = [a[0] for a in raw]
    y = [a[1] for a in raw]
    z = [a[2] for a in raw]
    return x, y, z

def gridGen(a, b):
    n = 0
    for i,v in enumerate(a):
        if a[i+1]-v>0.1:
            n = i+1
            break
    a1, b1 = [], []
    d = 1
    ta = range(0, len(a), n)
    eleA = np.array(a)[ta]
    eleAi = []
    for e in eleA:
        for t in range(d): eleAi.append(e+0.2*t/d)
    for i in range(n):
        #a1.append(list(np.array(a)[ta]))
        a1.append(eleAi)
        tb = [t+i for t in ta]
        eleB = np.array(b)[tb]
        eleBi = np.interp(eleAi, eleA, eleB)
        #b1.append(list(np.array(b)[tb]))
        b1.append(list(eleBi))
    return np.array(a1), np.array(b1)


x, y, z = loadData(filename)

x1, y1 = gridGen(x,y)
x1, z1 = gridGen(x,z)

fig = plt.figure(figsize=(12,12))
#ax = fig.gca(projection='3d')
cMap = cm.jet
#ax.plot_surface(x1, y1, z1, rstride=5, cstride=5, linewidth=0, cmap=cMap)
#cset = ax.contour(x1, y1, z1, stride=1,zdir='z', offset=1, linewidth=1, cmap=cMap)
#cset = ax.contourf(x1, y1, z1, stride=1,zdir='z', offset=1, linewidth=1, cmap=cMap)
plt.contourf(x1, y1, z1, linewidth=0, cmap=cMap)
#plt.contour(x1, y1, z1, linewidths=1, colors='black')
#plt.pcolormesh(x1,y1,z1, cmap=cMap)
plt.colorbar()

#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Z')
#ax.set_zlim(1,8)
plt.show()
