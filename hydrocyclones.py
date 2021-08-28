import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.integrate import quad


def DistrGranul(x, y, granulometry):
    if granulometry == "RRB":
        y = np.log(np.log(1/(1-y)))
    if granulometry == "GGS":
        y = np.log(y)
    if granulometry == "sigmoide":
        y = -np.log(1/y-1)
    
    x = np.log(x)
    model = LinearRegression().fit(x, y)
    m = model.coef_
    k = np.exp(-model.intercept_/m)
    r2 = model.score(x, y)
    return m, k, r2



def measures(dc, hydro, phydro):
  bc = dc*phydro["bc_dc"][hydro]
  do = dc*phydro["do_dc"][hydro]
  hc = dc*phydro["l_dc"][hydro]
  l = dc*phydro["lc_dc"][hydro]
  sc = dc*phydro["sc_dc"][hydro]
  return bc, do, hc, l, sc


# Corrigir Demco - bc = di, l = Sc, l1 = lc
def FeedVolumetricFlowRate(dc, dp, mu, rho, cv, hydro):
  if hydro == "Bradley":
    q = (dc*mu**(0.085)*dp**0.23*np.exp(0*cv)/(3.5*rho**0.31))**(1/0.54)
  if hydro == "Rietema":
    q = (dc*mu**0.028*dp**0.24*np.exp(-0.52*cv)/(4*rho**0.27))**(1/0.51)
  if hydro == "Demco4H":
    q = (dc*mu**0.028*dp**0.24*np.exp(-0.52*cv)/(4*rho**0.27))**(1/0.51)
  #q = 0.00133*dp**0.56*dc**0.21*bc**0.53*(l-sc)**0.16*(Du**2 + do**2)**0.49*np.exp(-0.31*cv)
  return q



def Reynolds(dc, mu, rho, q):
  Re = 4*rho*q/(np.pi*mu*dc)
  return Re



def Euler(cv, hydro, phydro, Re):
  Eu = phydro["k2"][hydro]*Re**phydro["n3"][hydro]*np.exp(phydro["n4"][hydro]*cv)
  #Eu = 43.5*dc^0.57*(dc/bc)^2.61*(dc/(do^2+du^2))^0.42*(dc/(l-sc))^0.98*Re^0.12*np.exp(-0.51*cv)
  return Eu



def WaterFlowRatio(dc, Du, Eu, hydro, phydro):
  Rw = phydro["k3"][hydro]*(Du/dc)**phydro["n5"][hydro]*Eu**phydro["n6"][hydro]
  #Rw = 1.18*(dc/do)^5.97*(du/dc)^3.10*Eu^(-0.54)
  return Rw



def StokesEulerNumber(cv, hydro, phydro, Rw):
  StkEu = phydro["k1"][hydro]*np.exp(phydro["n2"][hydro]*cv)*abs(np.log(1/Rw))**phydro["n1"][hydro]
  #np.log(Rw)**phydro["n1"][hydro]
  return StkEu



def ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu):
  d50 = np.sqrt(36*StkEu*mu*rho*q/(dp*dc*np.pi*(rhos-rho)))
  return d50



def ReducedEfficiency(x, a, m, k, d50, granulometry):
  if granulometry == "RRB":
    y = 1 - np.exp(-0.693*(k/d50)**a*np.log(1/(1-x))**(a/m))
  if granulometry == "GGS":
    y = 1 - np.exp(-0.693*(k/d50)**a*x**(a/m))
  if granulometry == "sigmoide":
    y = 1 - np.exp(-0.693*(k/d50)**a*(x/(1-x))**(a/m))
  return y



def underflow(cv, Et, Rw):
  cvu = Et*cv/(Rw-Rw*cv+Et*cv)
  return cvu



def calc(cv, dc, dp, Du, granulometry, k, mu, n, hydro, phydro, rho, rhos):
    result = []
    bc, do, hc, l, sc = measures(dc, hydro, phydro)
    q = FeedVolumetricFlowRate(dc, dp, mu, rho, cv, hydro)
    Re = Reynolds(dc, mu, rho, q)
    Eu = Euler(cv, hydro, phydro, Re)
    Rw = WaterFlowRatio(dc, Du, Eu, hydro, phydro)
    StkEu = StokesEulerNumber(cv, hydro, phydro, Rw)
    d50 = ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu)
    Etr, err = quad(ReducedEfficiency, 0, 1, args=(phydro["m"][hydro], n, k, 1e6*d50, granulometry))
    Et = Rw + Etr*(1 - Rw)
    cvu = underflow(cv, Et, Rw)
    result = [q, Re, Eu, Rw, StkEu, 1e6*d50, Etr, err, Et, cvu, bc, do, hc, l, sc]
    return result