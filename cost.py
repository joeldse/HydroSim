import numpy as np

def TotalCost(CEPCI, q):
    cp = CEPCI * 10**(3.6298 + 0.5009*np.log10(q) + 0.0411*np.log10(q)**2)/397
    return cp

def BareModuleCost(cp):
    CBM = 2.86 * cp
    return CBM

#round(CBM,-3)

