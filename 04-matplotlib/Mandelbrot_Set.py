import matplotlib.pyplot as plt
import numpy as np

# Mandelbrot_Set.py
__author__ = "Chuhang Liu"

# Setup
MaxInteration = 500
gridSize = 1000;
x = np.linspace(-2,2,gridSize)
y = np.linspace(-2,2,gridSize)
X, Y = np.meshgrid(x,y)
z0 = np.complex128(X + 1.0j*Y)

# Calculate
z = z0
for i in range(MaxInteration):
    z = z*z + z0
    inside = np.abs(z) <= 2.0
    #Inside = np.int32(inside)
    #print(Inside)
    #z = z * Inside
    #print(z)
    #inx,iny = np.where(np.abs(z)<=2)
#print(np.int32(inside)) 

# Show
inside = np.int32(inside)
ax = plt.gca()
ax.imshow(inside, extent=[-2, 2, -2, 2],cmap='viridis')
f1 = plt.gcf()
f1.set_size_inches(8,8)
	
plt.savefig("Mandelbrot_set.png")
