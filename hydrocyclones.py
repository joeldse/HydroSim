import numpy as np
import pandas as pd


def measures(dc, hydro, phydro):
  bc = dc*phydro["bc_dc"][hydro]
  do = dc*phydro["do_dc"][hydro]
  hc = dc*phydro["l_dc"][hydro]
  l = dc*phydro["lc_dc"][hydro]
  sc = dc*phydro["sc_dc"][hydro]
  return bc, do, hc, l, sc


def Reynolds(dc, mu, rho, q):
  Re = 4*rho*q/(np.pi*mu*dc)
  return Re



def Euler(cv, hydro, phydro, Re):
  Eu = phydro["k2"][hydro]*Re**phydro["n3"][hydro]*np.exp(phydro["n4"][hydro]*cv)
  return Eu



def WaterFlowRatio(dc, Du, Eu, hydro, phydro):
  Rw = phydro["k3"][hydro]*(Du/dc)**phydro["n5"][hydro]*Eu**phydro["n6"][hydro]
  return Rw



def StokesEulerNumber(cv, hydro, phydro, Rw): #bc = di, l = Sc, l1 = lc
  StkEu = phydro["k1"][hydro]*(np.log(1/Rw))**phydro["n1"][hydro]*np.exp(phydro["n2"][hydro]*cv)
  return StkEu



def ReducedCutSize(dc, dp, mu, q, rho, rhos, StkEu):
  d50 = np.sqrt(36*StkEu*mu*rho*q/(dp*dc*np.pi*(rhos-rho)))
  return d50







def Euler2(bc, cv, dc, du, do, l, Re, sc):
  Eu = 43.5*dc^0.57*(dc/bc)^2.61*(dc/(do^2+du^2))^0.42*(dc/(l-sc))^0.98*Re^0.12*np.exp(-0.51*cv)
  return Eu

def WaterFlowRatio2(dc, do, du, Eu):
  Rw = 1.18*(dc/do)^5.97*(du/dc)^3.10*Eu^(-0.54)
  return Rw
