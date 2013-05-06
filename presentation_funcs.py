import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate

def birthFunc(P, r):
    return (r * P)

def deathFunc(P, t, r, M):
    return ((r*(P/M))*P)

def priceFunc(quan):
    if ((40-.05*quan)>1):
        return (40-.05*quan)
    else:
        return 1

def costFunc(quan,var,fixed): #q, 10, 100
    return (fixed+var*quan)

def revFunc(quan):
    return (priceFunc(quan)*quan)

def profitFunc(quan, var, fixed):
    return (revFunc(quan)-costFunc(quan,var,fixed)) 

def unitProfit(quan, var, fixed):
    return (profitFunc(quan, var, fixed)/(quan+1))

def MR(quan):
    return (20-quan)

def MC(quan):
    return 10

def dEffort_dt(t):
    #print "t ",t
    return np.random.random()

#E(t)=.1*t
#E'(t) = .1
def effortFunc(t):
    prob_catch = np.random.random()
    return (prob_catch/(t+1))

def effortProfit(quan, var, fixed):
    prob_catch = np.random.random()
    return (prob_catch/(unitProfit(quan,var,fixed)))

def fishCaught(P,t,iteration):
    """
    fish caught with respect to time
    """
    return (effortFunc(t[iteration])*P)

def fishCaughtPi(P,quan,var,fixed): 
    """
    fish caught with respect to profit
    """
    return (effortProfit(quan,var,fixed)*P)

def dP_dt(P,t,r,M,iteration):
    return (birthFunc(P,r)-deathFunc(P,t,r,M)-fishCaught(P,t,iteration))

def dP_dpi(P,t,r,M,iteration,quan,var,fixed):
    return (birthFunc(P,r)-deathFunc(P,t,r,M)-fishCaughtPi(P,quan,var,fixed))


pop0 = 1000
birth_frac = 0.25
#death_frac = .2
carry_capac = 2000
variable_cost=10
fixed_cost=100

time_points = np.arange(1,49,1.)