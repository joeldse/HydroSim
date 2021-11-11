import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm

def graphic2D(df):
    des = 1
    return des



def graphic3D(df):
    fig = plt.figure()
    #  First subplot
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    graf=ax.plot_trisurf(df["d50"],100*df["Dc"], 100*df["Et"], cmap=cm.coolwarm, antialiased=True)

    fig.colorbar(graf, shrink=0.5, aspect=30, location='left')
    ax.set_xlabel(r'$d_{50} [\mu m]$')
    ax.set_ylabel(r'$D_c$ [cm]')
    ax.set_zlabel(r'$\eta$ [%]')

    # Second subplot
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    graf=ax.plot_trisurf(100*df["Cvu"],100*df["Dc"], 3600*df["Q"], cmap=cm.coolwarm, antialiased=True)

    fig.colorbar(graf, shrink=0.5, aspect=30, location='left')
    ax.set_xlabel(r'$C_{vu} [\%]$')
    ax.set_ylabel(r'$D_c$ [cm]')
    ax.set_zlabel(r'$Q [m^3/h]$')

    plt.show()
    return




#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
#https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html
