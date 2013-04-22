import numpy as np
import pandas as pd 
from scipy import integrate
import matplotlib.pyplot as plt

pop0=500
t = np.arange(10)
deltaPop = 0.25
p = 1

def growthFunc(pop0, deltaPop):
	return (deltaPop * pop0)

q = growthFunc(pop0, deltaPop)
w = 5
v = 10

def deathFunc(pop0,p,q,w,t,v,pc=0.5):
	return pop0-effort(p,q,w,t,v,pc)

def profit(p,q,w,t,v,pc=0.5):
	return (p*q*pc)-((w*t)-v)

def effort(p,q,w,t,v,probCatch=0.5):
	return (profit(p,q,w,t,v)*probCatch)

def expectedValue(p,q,w,t,v, pr=0.5):
	probCatch = effort(p,q,w,t,v,pr)
	return (probCatch*p)+(1-probCatch)*w

def dpop_dt(pop0, t, deltaPop, p, q, w, v, pc=0.5):
	return growthFunc(pop0,deltaPop)-deathFunc(pop0,p,q,w,t,v,pc)

#pop0 is a np.array
#t is an empty np.array or arange
fish_pop0 = integrate.odeint(dpop_dt, pop0, t, args=(deltaPop,p,q,w,t,v))

print pd.DataFrame(np.column_stack((t, fish_pop0, profit(p,q,w,t,v))),columns=["Days","Fish Pop","Profit"])

fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (Years)", ylabel="Fish Population/Profit in Dollars"), figsize=(8,5))
ax.plot(t, fish_pop0, "k", label="Fish", lw=2)
ax.plot(t, profit(p,q,w,t,v), "b", label="Profit", lw=2)
ax.legend()
plt.show()