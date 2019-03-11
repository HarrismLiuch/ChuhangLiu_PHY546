# 04-Q5
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np

num = 1000
x = np.linspace(0, 2.0*np.pi, num)
y = np.sin(x)

# subplot 1
plt.subplot(311)
plt.plot(x,y)
plt.xlabel("x",fontsize="large")
plt.ylabel("y",fontsize="large")

# subplot 2
plt.subplot(312)
dy = (y[1:] - y[:-1])/(2.0*np.pi/num)
plt.plot(x[:-1],dy)
plt.xlabel("x",fontsize="large")
plt.ylabel("y",fontsize="large")

# subplot 3
plt.subplot(313)
d2y = (dy[1:] - dy[:-1])/(2.0*np.pi/num)
plt.plot(x[:-2],d2y)
plt.xlabel("x",fontsize="large")
plt.ylabel("y''",fontsize="large")

# set size
f = plt.gcf()
f.set_size_inches(6,8)
