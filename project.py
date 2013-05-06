import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate

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

def simulationTime(P,t,r,M): #effort with respect to time
    data=np.zeros_like(t)
    for i in range(len(t)-1):
        if i==0:
            data[i]=dP_dt(P,t,r,M,i) + P
        else:
            data[i]=dP_dt(data[i-1],t,r,M,i)+data[i-1]
    return data


sim_time=simulationTime(pop0, time_points, birth_frac, carry_capac)

fish_data=pd.DataFrame(np.column_stack((time_points,sim_time)),columns=["Time (months)", "Fish"])
#print fish_data

fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Fish Population"))
ax.plot(time_points,sim_time, "k", lw=2)
plt.xlim(1,)
fig.suptitle("Fish Population (time based)")
plt.show()

def simulationProfit(P,t,r,M):
    data=np.zeros_like(t)
    fish_caught=np.zeros_like(t)
    for i in range(len(t)):
        if i==0:
            data[i]=dP_dpi(P,t,r,M,i,fish_caught[i],variable_cost,fixed_cost) + P
            fish_caught[i]=fishCaughtPi(P,0,variable_cost,fixed_cost)
        else:
            data[i]=dP_dpi(data[i-1],t,r,M,i,fishCaughtPi(P,fish_caught[i-1],variable_cost,fixed_cost),variable_cost,fixed_cost) + data[i-1]
            fish_caught[i]=fishCaughtPi(P,fish_caught[i-1],variable_cost,fixed_cost)
    return data

def demand(P,t,r,M):
    data=simulationProfit(P,t,r,M)
    demand=np.zeros_like(t)
    for i in range(len(t)):
        if i==0:
            demand[i]=fishCaughtPi(data[i],0,variable_cost,fixed_cost)
        else:
            demand[i]=fishCaughtPi(data[i],demand[i-1],variable_cost,fixed_cost)
    return demand

def priceInSim(P,t,r,M):
    prices=np.zeros_like(t)
    fish_caught=demand(P,t,r,M)
    for i in range(len(t)):
        if i==0:
            prices[i]=40
        else:
            prices[i]=priceFunc(fish_caught[i])
    return prices

sim_pi=simulationProfit(pop0, time_points,birth_frac,carry_capac)
dem=demand(pop0,time_points,birth_frac,carry_capac)
p_in_sim=priceInSim(pop0,time_points,birth_frac,carry_capac)

def average_price(prices):
    avg=0.0
    for e in prices:
        avg+=e
    return avg/len(prices)

def average_pop(pop):
    avg=0.0
    for e in pop:
        avg+=e 
    return avg/len(pop)

print "Average Price"
print average_price(p_in_sim)
print "Average Population"
print average_pop(sim_pi)

fish_pi_data=pd.DataFrame(np.column_stack((time_points,sim_pi,dem,p_in_sim)),columns=["Time (months)", "Fish","Demand","Price"])
print fish_pi_data
#fish_pi_data.save("/Users/Andreas/Desktop/test.txt")
#demand_data=pd.DataFrame(np.column_stack((time_points,dem)),columns=["Time (months)", "Demand"])
#print demand_data


fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Fish Population"))
ax.plot(time_points,sim_pi, "k", lw=2)
plt.xlim(1,)
fig.suptitle("Supply (Profit Based)")
plt.show()


fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Fish Demanded"))
ax.plot(time_points,dem, "b", lw=2)
plt.xlim(1,)
fig.suptitle("Demand")
plt.show()

fig, ax = plt.subplots(subplot_kw=dict(xlabel="Time (months)",ylabel="Price of Fish"))
ax.plot(time_points,p_in_sim, "g", lw=2)
plt.xlim(1,)
fig.suptitle("Price")
plt.show()
