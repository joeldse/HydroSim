#Bibliotecas
from parameters import *
from hydrocyclones import * 


# cálculo das variáveis
bc, do, hc, l, sc = measures(dc, hydro, phydro)
Re = Reynolds(dc, mu, rho, q)
Eu = Euler(cv, hydro, phydro, Re)
Rw = WaterFlowRatio(dc, Du, Eu, hydro, phydro)
StkEu = StokesEulerNumber(cv, hydro, phydro, Rw)
d50 = ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu)
m, k, r2 = DistrGranul(x_exp, y_exp, granulometry)


# Impressão dos resultados
print(f" Re: {Re:.2f}, Eu: {Eu:.2f}, Rw: {Rw:.2f}, StkEu: {StkEu:.2f}, d50: {d50*10**6:.2f}e-6")
print(m, k, r2)



# parametrização - Dc, Du, dP, Q, hydrocyclone

# links
# https://www.youtube.com/watch?v=GYFj52Jfkkg&list=PLsqyc_Q78CdhJ9WNATYaUs1oWk2bsdUuu