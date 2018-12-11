import math
import numpy as np
s = 100
k = 100
T = 1
v = .2
r = .06
div = .03
h = 99
n = 10
m = 100

def barrierOption(s,k,T,v,r,div,h,n,m):
    dt = T/n
    nudt = (r-div-.5 * v * v * dt)
    sigsdt = v * math.sqrt(dt)

    sum_Ct = 0
    sum_Ct2 = 0

    for j in range(m):
        St = s
        barrierCrossed = False
        for i in range(n):
            z1 = np.random.normal(size=m)
            z2 = -z1
            z = np.concatenate((z1, z2))
            St = St * max.exp(nudt + sigsdt * z)
            if St <= h:
                barrierCrossed = True
                break
        if barrierCrossed == True:
            Ct = 0
        else:
            Ct = np.max(0, St - k)
        sum_Ct += Ct
        sum_Ct2 += Ct*Ct
    callValue = sum_Ct/n * math.exp(-r*t)
    Sd = math.sqrt((sum_Ct2 - sum_Ct * sum_Ct/m) * math.exp(-2 * r * T) / (m-1))
    Se = Sd/math.sqrt(m)

    print(callValue)
    print(Sd)
    print(Se)

barrierOption(s,k,T,v,r,div,h,n,m)


def StratifiedSample(m = 100):
    u = np.random.uniform(size=m)  
    i = np.arange(m)
    uhat = (u + i) / m

    return uhat


def CallPayoff(s, k):
    return np.maximum(s - k, 0.0)

def StratifiedMonteCarloPricer(s,k,T,v,r,div,h,n,m):
    uhat = StratifiedSample(m)
    endval = norm.ppf(uhat)
    z = WienerBridge(T, m, steps, endval)
    
    spotT = np.zeros((m, n))
    spotT[:,0] = s
    
    dt = T / n
    nudt = (r-div-.5 * v * v * dt)
    sigsdt = v * math.sqrt(dt)
    
    for j in range(m):
        St = spot
        barrierCrossed = False
        for i in range(n):
            z1 = np.random.normal(size=m)
            z2 = -z1
            z = np.concatenate((z1, z2))
            St = St * max.exp(nudt + sigsdt * z)
            if St <= h:
                barrierCrossed = True
                break
        if barrierCrossed == True:
            Ct = 0
        else:
            Ct = np.max(0, St - k)
        sum_Ct += Ct
        sum_Ct2 += Ct*Ct


    callT = CallPayoff(spotT[:,-1], k)
    price = callT.mean() * np.exp(-r * T)
    
    return (price)
    #return price

## main
spot = 41.0
strike = 40.0
rate = 0.08
vol = 0.30
expiry = 1.0
div = 0.0
reps = 5
steps = 2 ** 2

StratifiedMonteCarloPricer(spot, strike, rate, vol, div, expiry, reps, steps)

