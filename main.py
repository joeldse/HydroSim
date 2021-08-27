#Bibliotecas
from hydrocyclones import *
from parameters import *

# Cálculo das variáveis
n, k, r2 = DistrGranul(x_exp, y_exp, granulometry)
bc, do, hc, l, sc = measures(dc, hydro, phydro)

def calc(cv, dc, dp, Du, granulometry, k, mu, n, hydro, phydro, rho, rhos):
    result = []
    q = FeedVolumetricFlowRate(dc, dp, mu, rho, cv, hydro)
    #q = FeedVolumetricFlowRate1(bc, cv, dc, do, dp, Du, l, sc)
    Re = Reynolds(dc, mu, rho, q)
    Eu = Euler(cv, hydro, phydro, Re)
    Rw = WaterFlowRatio(dc, Du, Eu, hydro, phydro)
    StkEu = StokesEulerNumber(cv, hydro, phydro, Rw)
    d50 = ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu)
    Etr, err = quad(ReducedEfficiency, 0, 1, args=(phydro["m"][hydro], n, k, 1e6*d50, granulometry))
    Et = Rw + Etr*(1 - Rw)
    cvu = underflow(cv, Et, Rw)
    result = [q, Re, Eu, Rw, StkEu, 1e6*d50, Etr, err, Et, cvu]
    return result

result = calc(cv, dc, dp, Du, granulometry, k, mu, n, hydro, phydro, rho, rhos)

print(f'Distribuição granulométrica: n = {n}, k = {k}, r² = {r2:.2f}')
print(f'Q = {result[0]:.5f}, Re = {result[1]:.0f}, d\u2085\u2080 = {result[5]:.2f}\u03BCm, \
Et\' = {result[6]:.2f}, Et = {result[8]:.2f}, c\u1D65\u1D64 = {result[9]:.2f}')



#cv, dc, dp, Du, mu, q, rho, rhos
# parametrização - Dc, Du, dP, hydrocyclone

#Familias: Bradley, Krebs, Rietema, Mozley, Dorr-Oliver

# links
# https://www.youtube.com/watch?v=GYFj52Jfkkg&list=PLsqyc_Q78CdhJ9WNATYaUs1oWk2bsdUuu
# portable: https://www.youtube.com/watch?v=QWqxRchawZY
# Tkinter: https://www.youtube.com/watch?v=ji8pTynQhEo
# portable: https://www.py2exe.org/index.cgi/SingleFileExecutable
