#Bibliotecas
from parameters import *
from granulometry import *
from hydrocyclones import * 
import numpy as np


# cálculo das variáveis
bc, do, hc, l, sc = measures(dc, hydro, phydro)
Re = Reynolds(dc, mu, rho, q)
Eu = Euler(cv, hydro, phydro, Re)
Rw = WaterFlowRatio(dc, Du, Eu, hydro, phydro)
StkEu = StokesEulerNumber(cv, hydro, phydro, Rw)        #diverse um pouco
d50 = ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu)


# Impressão dos resultados
print(Re, Eu, Rw, StkEu, d50)
print(phydro["n1"][hydro])
print(data.iloc[0,1])
print(phydro["k1"][hydro])

# continuar em WaterFlowRatio
# parametrização - Dc, Du, dP, Q, hydrocyclone
