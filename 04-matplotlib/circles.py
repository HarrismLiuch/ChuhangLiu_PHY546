#04-Q3
__author__ = "Chuhang Liu"

import matplotlib.pyplot as plt
import numpy as np
import random

def draw_circle(x0, y0, R, color):
    '''
    (x0, y0) is the center of the circle
    R is the radius
    and color is the color of the circle
    valid color arguments are:
    'b': blue
    'g': green
    'r': red
    'c': cyan
    'm': magenta
    'y': yellow
    'k': black
    'w': white
    '''
    theta = np.linspace(0, 2.0*np.pi, 1000)
    # create x, y
    x = R * np.cos(theta) + x0
    y = R * np.sin(theta) + y0
    # plot
    plt.plot(x,y,color)


colors = ['b','g','r','c','m','y','k','w']
for i in range(10):
    x0 = 20*random.random() - 10
    y0 = 20*random.random() - 10
    R = random.random()*2
    color_index = random.randrange(len(colors))
    draw_circle(x0,y0,R,colors[color_index])

# set figure size
f = plt.gcf()
f.set_size_inches(6,6)
# set x,y limit
plt.xlim(-12.0,12.0)
plt.ylim(-12.0,12.0)
