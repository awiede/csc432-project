import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
import random

#population = P
#instantaneous growth rate = r
#dP/dt = rP
#initial pop = pop0
#P=pop0 * e **(r*t)
#deltapop = P(t)-P(t-dt) = (r*P(t-dt))*dt
#carrying capacity = M
#number of deaths = D
#dD/dt = (r * (P/M))*P
#dP/dt = (r*P) - (r * (P/M))*P = r*(1-(P/M))*P


def birthFunc(P, r):
    return (r * P)

def deathFunc(P, t, r, M):
    return ((r*(P/M))*P)

def priceFunc(q):
    if ((10-.5*q)>1):
        return (10-.5*q)
    else:
        return 1

def costFunc(q):
    return (100+10*q)

def revFunc(q):
    return (priceFunc(q)*q)

def profitFunc(q):
    return (revFunc(q)-costFunc(q)) 

def unitProfit(q):
    return (profitFunc(q)/q)

def MR(q):
    return (10-q)

def MC(q):
    return 10

#E(t)=.1*t
#E'(t) = .1
def effortFunc(t):
    #why does the np.random raise an error?
    #replaced with python random, slower I think.
    prob_catch = np.random.random()
    return (prob_catch/(t+1))

def dEffort_dt(t):
    #print "t ",t
    return np.random.random()

def fishCaught(P,t,iteration):
    return (effortFunc(t[iteration])*P)

def dP_dt(P,t,r,M,iteration):
    return (birthFunc(P,r)-deathFunc(P,t,r,M)-fishCaught(P,t,iteration))

pop0 = 1000
birth_frac = 0.25
#death_frac = .2
carry_capac = 2000

time_points = np.arange(1,49,1.)
print time_points

def simulation(P,t,r,M):
    data=np.zeros_like(t)
    for i in range(len(t)-1):
        if i==0:
            data[i]=dP_dt(P,t,r,M,i) + P
        else:
            data[i]=dP_dt(data[i-1],t,r,M,i)+data[i-1] #this is the change in pop. not total pop
    return data

sim=simulation(pop0, time_points, birth_frac, carry_capac)
#pops = integrate.odeint(dP_dt, pop0, time_points, args=(birth_frac, carry_capac))

fish_data=pd.DataFrame(np.column_stack((time_points,sim)),columns=["Time (months)", "Fish"])
print fish_data

fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Fish Population"))
ax.plot(time_points,sim, "k", lw=2)
#ax.plot(time_points,)
plt.xlim(1,)
fig.suptitle("Fish Population")
plt.show()