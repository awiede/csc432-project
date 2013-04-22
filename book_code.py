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

def deathFunc(P, r, M):
	return ((r*(P/M))*P)

def dP_dt(P,t,r,M):
	return (birthFunc(P,r)-deathFunc(P,r,M))


pop0 = 100
birth_frac = 2.
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