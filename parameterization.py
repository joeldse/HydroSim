
#3D plots as subplots
import pandas as pd
from hydrocyclones import *


def parameterization(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos, interval):
    df = pd.DataFrame()
    for i in range(interval):
        d1 = 0.9*dc + 0.2*i*dc/(interval-1)
        for j in range(interval):
            d2 = 0.9*Du + 0.2*i*Du/(interval-1)
            for t in range(1, interval+1):
                d3 = 0.9*dp + 0.2*i*dp/(interval-1)
                x = calc(cv, d1, d3, d2, granulometry, family, k, mu, n, phydro, qt, rho, rhos)
                df = df.append({'dc': d1, 'Du': d2, 'dp': d3, 'Q': x[0], 'Re': x[1], 'd50': x[5], 'Et_red': x[6], 
                'Et': x[8], 'cvu': x[9], 'n_hydro': x[15], 'cp': x[16], 'cbm': x[17]}, ignore_index=True)
    return df
