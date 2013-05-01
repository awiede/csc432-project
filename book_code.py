import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import random

"""
population = P
instantaneous growth rate = r
dP/dt = rP
initial pop = pop0
P=pop0 * e **(r*t)
deltapop = P(t)-P(t-dt) = (r*P(t-dt))*dt
carrying capacity = M
number of deaths = D
dD/dt = (r * (P/M))*P
dP/dt = (r*P) - (r * (P/M))*P = r*(1-(P/M))*P
"""

def birthFunc(P, r):
    return (r * P)

def deathFunc(P, t, r, M):
    return ((r*(P/M))*P)

def priceFunc(quan):
    if ((20-.05*quan)>1):
        return (20-.05*quan)
    else:
        return 1

def costFunc(quan,var,fixed): #q, 10, 100
    return (fixed+var*quan)

def revFunc(quan):
    return (priceFunc(quan)*quan)

def profitFunc(quan, var, fixed):
    return (revFunc(quan)-costFunc(quan,var,fixed)) 

def unitProfit(quan):
    return (profitFunc(quan)/quan)

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
    return (profitFunc(quan,var,fixed)*prob_catch)

def fishCaught(P,t,iteration):
    """
    fish caught with respect to time
    """
    return (effortFunc(t[iteration])*P)

def fishCaughPi(P,quan,var,fixed): 
    """
    fish caught with respect to profit
    """
    return (effortProfit(quan,var,fixed)*P)

def dP_dt(P,t,r,M,iteration):
    return (birthFunc(P,r)-deathFunc(P,t,r,M)-fishCaught(P,t,iteration))

def dP_dpi(P,t,r,M,iteration,quan,var,fixed):
    return (birthFunc(P,r)-deathFunc(P,t,r,M)-fishCaught(P,t,iteration))

pop0 = 1000
birth_frac = 0.25
#death_frac = .2
carry_capac = 2000

time_points = np.arange(1,49,1.)
print time_points

def simulationTime(P,t,r,M): #effort with respect to time
    data=np.zeros_like(t)
    for i in range(len(t)-1):
        if i==0:
            data[i]=dP_dt(P,t,r,M,i) + P
        else:
            data[i]=dP_dt(data[i-1],t,r,M,i)+data[i-1]
    return data

sim_time=simulationTime(pop0, time_points, birth_frac, carry_capac)
#pops = integrate.odeint(dP_dt, pop0, time_points, args=(birth_frac, carry_capac))

fish_data=pd.DataFrame(np.column_stack((time_points,sim_time)),columns=["Time (months)", "Fish"])
print fish_data

fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Fish Population"))
ax.plot(time_points,sim_time, "k", lw=2)
#ax.plot(time_points,)
plt.xlim(1,)
fig.suptitle("Fish Population")
plt.show()

def simulationProfit(P,t,r,M):
    data=np.zeros_like(t)
    for i in range(len(t)):
        data[i]=func 
    return data

