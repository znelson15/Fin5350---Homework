import numpy as np

def callPayoff(spot, strike):
    return np.maximum(spot - strike, 0.0)

def putPayoff (spot, strike):
    return np.maximum(strike - spot, 0.0)

r = .08
v = .3
q = 0.0
expiry = 1.0
n = 1.0
h = eqpiry / n
S = 100
K = 95

u = exp{}