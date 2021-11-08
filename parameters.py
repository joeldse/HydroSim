import numpy as np
import pandas as pd
import configparser

#recolhimento de dados experimentais
config = configparser.ConfigParser()
config.read("properties.conf")

for experiment in config.sections():
    file = config.get(experiment, "file")

# experimental values of granulometry
data = pd.read_csv(file, sep=',')
x_exp = np.array(data.iloc[:,0].to_frame().T).reshape((-1, 1))
y_exp = np.array(data.iloc[:,1])



for experiment in config.sections():
    file = config.get(experiment, "fileresults")
# experimental values of granulometry
data = pd.read_csv(file, sep=',')
x_res = np.array(data.iloc[0,0])
y_res = np.array(data.iloc[:,1])



# Hydrocyclone constants
phydro = pd.DataFrame(
  {
    "bc_dc": [0.28, 1/7, 0.26],
    "do_dc": [0.34, 1/5, 0.33],
    "l_dc": [5, 0, 3.3],
    "lc_dc": [0, 1/2, 0.55],
    "sc_dc": [0.4, 1/3, 0.55],
    "theta": [20, 9, 20],
    "k1": [0.0474, 0.0550, 0.0088],
    "k2": [371.5, 258, 3300],
    "k3": [1218, 1.21e6, 0.127],
    "n1": [0.74, 0.66, 2.31],
    "n2": [9.0, 12.0, 15.5],
    "n3": [0.12, 0.37, 0.00],
    "n4": [-2.12, 0.00, 0.00],
    "n5": [4.75, 2.63, 0.78],
    "n6": [-0.30, -1.12, 0.00],
    "m": [2.45, 3.12, 3.30],
  }, index= ["Rietema", "Bradley", "Demco4H"]
)



