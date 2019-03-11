# 04-Q2
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2.0*np.pi, 1000)
# set radius R
R = 1
# create x, y
x = R*np.cos(theta)
y = R*np.sin(theta)
# plot
plt.plot(x,y,"g")
# set figure size
f = plt.gcf()
f.set_size_inches(6,6)
# fill the circle
ax = plt.gca()
ax.fill(x, y, "r")
