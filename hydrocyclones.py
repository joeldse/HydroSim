import numpy as np

class ConfHidro:
  def __init__(self, name, bc_dc, do_dc, l_dc, lc_dc, sc_dc, theta):
    self.name = name
    self.bc_dc = bc_dc
    self.do_dc = do_dc
    self.l_dc = l_dc
    self.lc_dc = lc_dc
    self.sc_dc = sc_dc
    self.theta = theta


def measures(dc, hydro):
  bc = dc*hydro.bc_dc
  do = dc*hydro.do_dc
  hc = dc*hydro.l_dc
  l = dc*hydro.lc_dc
  sc = dc*hydro.sc_dc
  return bc, do, hc, l, sc


def Reynolds(dc, mu, q, rho):
  Re = 4*rho*q/(np.pi*mu*dc)
  return Re


def Euler(cv, hydro, Re):
  if hydro == "Rietema":
    k2 = 317.5; n3 = 0.12; n4 = -2.12;
  if hydro == "Bradley":
    k2 = 258; n3 = 0.37; n4 = 0.00;
  if hydro == "Demco4H":
    k2 = 3300; n3 = 0.00; n4 = 0.00;

  Eu = k2*Re^n3*np.exp(n4*cv)
  return Eu


def Euler2(bc, cv, dc, du, do, l, Re, sc):
  Eu = 43.5*dc^0.57*(dc/bc)^2.61*(dc/(do^2+du^2))^0.42*(dc/(l-sc))^0.98*Re^0.12*np.exp(-0.51*cv)
  return Eu


def WaterFlowRatio(dc, do, du, Eu):
  Rw = 1.18*(dc/do)^5.97*(du/dc)^3.10*Eu^(-0.54)
  return Rw


def StkEu(cv, dc, do, l, rw, sc): #bc = di, l = Sc, l1 = lc
  StkEu = 0.12*(dc/do)^0.95*(dc/(l-sc))^1.33*(np.log(1/rw))^0.79*np.exp(12.0*cv)
  return StkEu


def du(dc, do, dp, rho, q, rw):
  du = 0.983*(dc^1.926/do^0.229)*(dp/(rho*q^2))^0.174*rw^0.323
  return du

