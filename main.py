# Libraries
import numpy as np
from hydrocyclones import *
from parameters import *
from parameterization import *


# Calculation of variables
n, k, r2 = DistrGranul(x_exp, y_exp, granulometry)
result = calc(cv, dc, dp, Du, granulometry, family, k, mu, n, phydro, qt, rho, rhos)
df = parameterization(cv, dc, dp, Du, granulometry, k, mu, n, family, phydro, qt, rho, rhos)


# printing of results
print(f'Distribuição granulométrica: n = {n}, k = {k}, r² = {r2:.2f}')
print(f'Q = {result[0]:.6f}, Re = {result[1]:.0f}, d\u2085\u2080 = {result[5]:.2f}\u03BCm, \
Et\' = {result[6]:.2f}, Et = {result[8]:.2f}, c\u1D65\u1D64 = {result[9]:.3f}, n° Hidroc: {int(np.ceil(result[15]))}')
print(df.to_string())
#graphic(df)

# cv, dc, dp, Du, mu, q, rho, rhos
# correção da equação de vazão
# interface: https://cadernodelaboratorio.com.br/pygubu-tkinter-mais-facil/
# parametrização - Dc, Du, dP, hydrocyclone (intevalo, D_inicial, D_final) - recomendado: entre 10 e 20 (1000 - 10s)
# gráficos: [Du, Dc, Et], [cvu, Dc, cost]
# Familias: Bradley, Krebs, Rietema, Mozley, Dorr-Oliver

# links:
# https://www.youtube.com/watch?v=GYFj52Jfkkg&list=PLsqyc_Q78CdhJ9WNATYaUs1oWk2bsdUuu
# portable: https://www.youtube.com/watch?v=QWqxRchawZY
# Tkinter: https://www.youtube.com/watch?v=ji8pTynQhEo
# portable: https://www.py2exe.org/index.cgi/SingleFileExecutable
