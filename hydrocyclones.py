import numpy as np

#phydro["k1"]["Rietema"]

def measures(dc, hydro):
  bc = dc*hydro["bc_dc"]
  do = dc*hydro.do_dc
  hc = dc*hydro.l_dc
  l = dc*hydro.lc_dc
  sc = dc*hydro.sc_dc
  return bc, do, hc, l, sc


def Reynolds(dc, mu, rho, q):
  Re = 4*rho*q/(np.pi*mu*dc)
  return Re


def Euler(cv, phydro, Re):
  Eu = (phydro.k2)*Re^(phydro.n3)*np.exp((phydro.n4)*cv)
  return Eu



def WaterFlowRatio(dc, du, Eu, hydro):
  if hydro == "Rietema":
    k3 = 1218; n5 = 4.75; n6 = -0.30;
  if hydro == "Bradley":
    k3 = 1.21*10^6; n5 = 2.63; n6 = -1.12;
  if hydro == "Demco4H":
    k3 = 0.127; n5 = 0.78; n5 = 0.00;

  Rw = k3*(du/dc)^n5*Eu^n6
  return Rw



def StkEu(cv, dc, do, l, rw, sc): #bc = di, l = Sc, l1 = lc
  StkEu = 0.12*(dc/do)^0.95*(dc/(l-sc))^1.33*(np.log(1/rw))^0.79*np.exp(12.0*cv)
  return StkEu


def du(dc, do, dp, rho, q, rw):
  du = 0.983*(dc^1.926/do^0.229)*(dp/(rho*q^2))^0.174*rw^0.323
  return du





def Euler2(bc, cv, dc, du, do, l, Re, sc):
  Eu = 43.5*dc^0.57*(dc/bc)^2.61*(dc/(do^2+du^2))^0.42*(dc/(l-sc))^0.98*Re^0.12*np.exp(-0.51*cv)
  return Eu

def WaterFlowRatio2(dc, do, du, Eu):
  Rw = 1.18*(dc/do)^5.97*(du/dc)^3.10*Eu^(-0.54)
  return Rw
