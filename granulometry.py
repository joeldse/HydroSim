import numpy as np
from sklearn.linear_model import LinearRegression


def LRegression(x, y):
    #x, y = np.array(x), np.array(y)
    model = LinearRegression().fit(x, y)
    return model



def rrb(x, y):
    x = np.log(x)
    y = np.log(np.log(1/(1-y)))
    model = LRegression(x, y)
    m = model.coef_
    k = np.exp(-model.intercept_/m)/1e6
    r2 = model.score(x, y)
    return m, k, r2


def ggs(x, y):
    x = np.log(x)
    y = np.log(y)
    model = LRegression(x, y)
    m = model.coef_
    k = np.exp(-model.intercept_/m)/1e6
    r2 = model.score(x, y)
    return m, k, r2


def sigmoide(x, y):
    x = np.log(x)
    y = -np.log(1/y-1)
    model = LRegression(x, y)
    m = model.coef_
    k = np.exp(-model.intercept_/m)/1e6
    r2 = model.score(x, y)
    return m, k, r2