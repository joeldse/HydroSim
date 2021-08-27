
#3D plots as subplots

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data
from matplotlib import cm
import numpy as np


fig = plt.figure(figsize=plt.figaspect(0.5))

#  First subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

X = np.linspace(-6, 6, 60)  #[-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
Y = np.linspace(-6, 6, 60)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=1, antialiased=False)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, location='left', aspect=30)
ax.set_xlabel(r'$D_c$ [cm]')
ax.set_ylabel(r'$D_u$ [cm]')
ax.set_zlabel(r'$\eta$ [%]')


# Second subplot
ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()




#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
#https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html
