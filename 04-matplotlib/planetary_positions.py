# 04-Q1
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np

# Setup
a = np.array([0.39, 0.72, 1.00, 1.52, 5.20, 9.54, 19.22, 30.06, 39.48])
P = np.array([0.24, 0.62, 1.00, 1.88, 11.86, 29.46, 84.01, 164.8, 248.09])
names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# Plot
plt.plot(a,P,"ro")
ax = plt.gca()
# log scale
ax.set_yscale("log")
ax.set_xscale("log")
f = plt.gcf()
# set size
f.set_size_inches(8,6)
# set label
ax.set_xlabel("distance")
ax.set_ylabel("period")
# add text
for i in range(len(names)):
    plt.text(a[i], P[i], names[i])
