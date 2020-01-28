#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:18:03 2019

@author: benjamin.harney
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits import mplot3d

#Vectorizing the partial differential equations that characterize the 3-D magnus effect
def f(Z,t):
    x,Vx,y,Vy,z,Vz = Z
    v = np.sqrt(Vx**2 + Vy**2 + Vz**2)
    dx = Vx
    dVx = -(B0/m)*abs(v)*Vx + (S0/m)*((Wy*Vz)-(Wz*Vy))
    dy = Vy
    dVy = -g - (B0/m)*abs(v)*Vy + (S0/m)*((Wz*Vx)-(Wx*Vz))
    dz = Vz
    dVz = -(B0/m)*abs(v)*Vz + (S0/m)*((Wx*Vy)-(Wy*Vx))
    return [dx,dVx,dy,dVy,dz,dVz]

#Initial conditions
B0 = 6.33e-4
theta = np.radians(45)
phi = np.radians(0)
m = 2.2
S0 = .1
g = 9.81

time = np.linspace(0,10,1000)
v_init = 45
Wx,Wy,Wz = [0,0,5]
init = [0,v_init*np.sin(theta)*np.cos(phi),0,v_init*np.cos(theta),0,v_init*np.sin(theta)*np.sin(phi)]

#solving the differential equations using odeint
soln = odeint(f,init,time)

#assigning variable solutions
x,Vx,y,Vy,z,Vz = soln[:,0], soln[:,1], soln[:,2], soln[:,3], soln[:,4], soln[:,5]

#Plotting the solutions
plt.figure()
ax = plt.axes(projection='3d')
ax.plot(z,x,y,label='3-D Trajectory')
ax.set_xlabel('z-position')
ax.set_ylabel('x-position')
ax.set_zlabel('Y-position')
ax.set_title('3-D Position Plot')
plt.show()

plt.figure()
plt.plot(x,y,label='2-D Trajectory')
plt.xlabel('X-Position')
plt.ylabel('Y-Position')
plt.suptitle('2-D Position Plot')
plt.legend()
plt.show()

plt.figure()
plt.plot(Vx,Vy,label='2-D velocity') 
plt.xlabel('X-velocity')
plt.ylabel('Y-Velocity')
plt.suptitle('2-D velocity plot')
plt.legend()
plt.show()

