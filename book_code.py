import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate 

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
	#why does the random raise an error?
	prob_catch = np.random.random()
	return (unitProfit(t)*prob_catch)

def dP_dt(P,t,r,M):
	return (birthFunc(P,r)-deathFunc(P,t,r,M)-(effortFunc(t)*P))


pop0 = 100
birth_frac = 5.
#death_frac = .2
carry_capac = 500

time_points = np.arange(0,10,1.)

pops = integrate.odeint(dP_dt, pop0, time_points, args=(birth_frac, carry_capac))

fish_data=pd.DataFrame(np.column_stack((time_points,pops)),columns=["time", "Fish"])
print fish_data

fig, ax = plt.subplots(subplot_kw=dict(xlabel="time",ylabel="fish population"))
ax.plot(time_points,pops, "k", lw=2)
fig.suptitle("Fish Population")
plt.show()