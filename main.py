#Bibliotecas
import pandas as pd
import configparser
from hydrocyclones import * 
from granulometry import *
#from sklearn.linear_model import LinearRegression


#Configurações e parâmetros     #l = Sc, l1 = lc
Rietema = ConfHidro('Rietema', 0.28, 0.34, 5, 0, 0.4, 20)
Bradley = ConfHidro('Bradley', 1/7, 1/5, 0, 1/2, 1/3, 9)
Demco4H = ConfHidro('Demco 4H', 0.26, 0.33, 3.3, 0.55, 0.55, 18)



#recolhimento de dados experimentais
config = configparser.ConfigParser()
config.read("properties.conf")

for experiment in config.sections():
    file = config.get(experiment, "file")
    hydrocyclone = config.get(experiment, "hydrocyclone")
    q = config.getfloat(experiment, "Q")
    rho = config.getfloat(experiment, "rho")
    mu = config.getfloat(experiment, "mu")
    dc = config.getfloat(experiment, "Dc")
    cv = config.getfloat(experiment, "cv")

data = pd.read_csv(file, sep=';')
#data = pd.read_excel('Dados experimentais.xlsx')

hydrocyclone = Rietema

print(data)
print(data.iloc[0,1])
print(hydrocyclone.lc_dc)
x = rrb()
print(x[1])

bc, do, hc, l, sc = measures(dc, hydrocyclone)
print(bc,do)
print(measures(dc, hydrocyclone))

#reg = LinearRegression().fit(X, y)
#reg.score(x, y)

# parametrização - use vazão, queda de pressão, Du e Dc