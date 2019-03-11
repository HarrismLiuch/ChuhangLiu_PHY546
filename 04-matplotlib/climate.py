# 04-Q4
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np

filename = 'nasa-giss.txt'
a = np.loadtxt(filename)
#plot smoothed representation of the temperature change
plt.plot(a[:,0],a[:,2],'g')
ax = plt.gca()
#plot the temperature change
for i in range((a[:,0]).shape[0]):
    if a[i,1] >= 0:
        ax.plot(a[i,0],a[i,1],'r.')
    if a[i,1] < 0:
        ax.plot(a[i,0],a[i,1],'b.')

