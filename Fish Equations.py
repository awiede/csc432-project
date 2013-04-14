# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# $\textbf{Fish Population}$
# 
# Growth Rate
# 
# Growth over time period: $t$
# 
# Growth Rate: $deltaPop$
# 
# Initial Population: $pop0$ 
# 
# $\displaystyle newPop = \frac{deltaPop \times pop0}{t}$

# <codecell>

def growthFunc(pop0, deltaPop, t):
    from __future__ import division
    return (deltaPop * pop0)/(t) 

# <markdowncell>

# $\textbf{Profit Function}$
# 
# Price of fish: $p$
# 
# Quantity of fish: $q$
# 
# Labor cost: $w$
# 
# Time: $t$
# 
# Fixed Capital cost: $v$
# 
# Profit: $\pi$
# 
# $\pi = (p \times q) - ((w \times t) + v)$

# <codecell>

def profit(p, q, w, t, v):
    return (p*q)-((w*t)-v)

# <markdowncell>

# $\textbf{Effort Function}$
# 
# For this model, assume that each fisher is self employed and thus individual effort function is dependent upon profit such that
# 
# Effort, $E(\pi, probCatch) = \pi \times probCatch$

# <codecell>

def effort(p, q, w, t, v, probCatch=0.5):
    return profit(p, q, w, t, v)*probCatch

# <markdowncell>

# $\textbf{Expected Value }$ as a part of the effort function
# 
# Probability of catching a fish during time t: $probCatch$
# 
# Expected Value equation: $probCatch \times profit + (1-probCatch) \times - w$
# 
# Where $probCatch$ is the result of the effort function.

# <codecell>

def expectedValue(p, q, w, t, v, pr=0.5):
    probCatch = effort(p, q, w, t, v, pr=0.5)
    return probCatch*p+(1-probCatch)*w

# <markdowncell>


