#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:26:17 2019

@author: benjamin.harney
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



def R(Y, t, alpha, beta):
    r, f = Y
    xdot = r - r * f - alpha * r ** 2
    ydot = r * f - beta * f
    return [xdot, ydot]

alpha = 0.2
beta = .915


time = np.linspace(0, 150, 100000)
y_init = [1,1]

soln = odeint(R,y_init,time,args=(alpha, beta,))

r, f = soln[:,0], soln[:,1]


fig,(ax1,ax2) = plt.subplots(2,figsize=(8,6))

ax1.plot(time,r,label='Rabbits')
ax1.plot(time,f,label='Foxes')
ax1.set_xlabel('Time')
ax1.set_ylabel('Density of Animals')
ax1.legend(loc='upper right')

ax2.set_xlabel('Density of Rabbits')
ax2.set_ylabel('Density of Foxes')
ax2.plot(r, f)
plt.show()

print(r[0],r[-1],f[0],f[-1])
print(np.min(r),np.max(r))
print(np.min(f),np.max(f))