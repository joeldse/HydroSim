#Bibliotecas
from parameters import *
from hydrocyclones import * 


# cálculo das variáveis       #cv, dc, dp, Du, mu, q, rho, rhos
bc, do, hc, l, sc = measures(dc, hydro, phydro)
q = FeedVolumetricFlowRate(dc, dp, mu, rho, cv, hydro)
Re = Reynolds(dc, mu, rho, q)
Eu = Euler(cv, hydro, phydro, Re)
Rw = WaterFlowRatio(dc, Du, Eu, hydro, phydro)
StkEu = StokesEulerNumber(cv, hydro, phydro, Rw)
d50 = ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu)
n, k, r2 = DistrGranul(x_exp, y_exp, granulometry)
Etr, err = quad(ReducedEfficiency, 0, 1, args=(phydro["m"][hydro], n, k, 1e6*d50, granulometry))
Et = Rw + Etr*(1 - Rw)
cvu = underflow(cv, Et, Rw)

# Impressão dos resultados
print(f" Q: {q:.6f} Re: {Re:.2f}, Eu: {Eu:.2f}, Rw: {Rw:.2f}, StkEu: {StkEu:.2f}, d50: {d50*10**6:.2f}\u03BCm, Et = {Et:.2f}")
print(n, k, r2)
print(Etr, err, Et, cvu)
print(qt)



# parametrização - Dc, Du, dP, hydrocyclone

#Families: Bradley, Krebs, Rietema, Mozley, Dorr-Oliver

# links
# https://www.youtube.com/watch?v=GYFj52Jfkkg&list=PLsqyc_Q78CdhJ9WNATYaUs1oWk2bsdUuu
# portable: https://www.youtube.com/watch?v=QWqxRchawZY
# Tkinter: https://www.youtube.com/watch?v=ji8pTynQhEo
# portable: https://www.py2exe.org/index.cgi/SingleFileExecutable
