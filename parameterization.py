
#3D plots as subplots
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib import cm
from hydrocyclones import *

def parameterization(cv, dc, dp, Du, granulometry, k, mu, n, hydro, phydro, rho, rhos):
    interval = 5; dc = 0.06; dcf = 0.1;  Du = 0.006; Duf = 0.015; dp = 344750.0; dpf = 349750.0
    df = pd.DataFrame({'Dc' : []})
    for i in range(1,interval+1):
        dc = dc + (i-1)*(dcf-dc)/2
        for j in range(1,interval+1):
            Du = Du + (j-1)*(Duf - Du)/2
            for t in range(1, interval+1):
                dp = dp + (t-1)*(dpf - dp)/2
                x = calc(cv, dc, dp, Du, granulometry, k, mu, n, hydro, phydro, rho, rhos)
                df = df.append({'Dc': dc, 'Du': Du, 'dP': dp, 'Q': x[0], 'Re': x[1], 'd50': x[5], 
                'Cvu': x[9], 'Et\'': x[6], 'Et': x[8], 'Bc': x[10], 'Do': x[11], 'Hc': x[12],
                'L': x[13], 'Sc': x[14]}, ignore_index=True)
    return df



def graphic(df):
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



def graphic2D(df):
    des = 1
    return des






#https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html
#https://matplotlib.org/stable/gallery/subplots_axes_and_figures/colorbar_placement.html
