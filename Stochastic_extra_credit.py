#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 21:37:51 2019

@author: benjamin.harney
"""

from numpy.random import random
import numpy as np
import matplotlib.pyplot as plt

def decay_step(num,prob):
    num_decays = 0
    for i in range(num):
        if random() < prob:
            num_decays += 1
            
    return num_decays

def decay_step_2(num,prob_decay,prob_species):
    number_Polonium212 = 0
    number_Thallium208 = 0
    for i in range(num):
        if random() < prob_decay:
            if random() < prob_species:
                number_Polonium212 += 1
            else:
                number_Thallium208 +=1
                
            
    return number_Polonium212,number_Thallium208
    
# Half-lives of the isotopes
tau_Rn220 = 55.6    #Half-life of Radon
tau_Po216 = 0.145   #Half-life of Polonium 216
tau_Pb212 = 38304   #Half-life of Lead 212
tau_Bi212 = 3633    #Half-life of Bismuth 212
tau_Po212 = 2.99e-7 #Half-life of Polonium 212
tau_Tl208 = 183.18  #Half-life of Thallium208


# Initial number of atoms
initial = 1000      # Initial # of species

# A maximum of 10 half-lives is good.
# Number of steps should always be much larger than max time.
time,step = np.linspace(0,4.3e5,1000000,retstep="true")

prob_Polonium212 = 0.6406               #Probability of Bismuth decaying to Polonium
prob1 = 1-2**(-step/tau_Rn220)          #Probability of Radon 220 decay
prob2 = 1-2**(-step/tau_Po216)          #Probability of Polonium 216 decay
prob3 = 1-2**(-step/tau_Pb212)          #Probability of Lead 212 decay
prob4 = 1-2**(-step/tau_Bi212)          #Probability of Bismuth 212 decay
prob5 = 1-2**(-step/tau_Po212)          #Probability of Polonium 212 decay
prob6 = 1-2**(-step/tau_Tl208)          #Probability of Thallium 208 decay

#Abundances of the isotopes
N_Rn220 = np.zeros(len(time),int)
N_Po216 = np.zeros(len(time),int)
N_Pb212 = np.zeros(len(time),int)
N_Bi212 = np.zeros(len(time),int)
N_Po212 = np.zeros(len(time),int)
N_Tl208 = np.zeros(len(time),int)
N_Pb208 = np.zeros(len(time),int)
N_Rn220[0] = initial


for t in range(1,len(time)):
    decay_Bi212_Po212,decay_Bi212_Tl208 = decay_step_2(N_Bi212[t-1],prob4,prob_Polonium212)
    decay_Rn220_Po216 = decay_step(N_Rn220[t-1],prob1)
    decay_Po216_Pb212 = decay_step(N_Po216[t-1],prob2)
    decay_Pb212_Bi212 = decay_step(N_Pb212[t-1],prob3)
    decay_Po212_Pb208 = decay_step(N_Po212[t-1],prob5)
    decay_Tl208_Pb208 = decay_step(N_Tl208[t-1],prob6)
    N_Pb208[t] = N_Pb208[t-1] + decay_Tl208_Pb208 + decay_Po212_Pb208
    N_Tl208[t] = N_Tl208[t-1] - decay_Tl208_Pb208 + decay_Bi212_Tl208
    N_Po212[t] = N_Po212[t-1] - decay_Po212_Pb208 + decay_Bi212_Po212
    N_Bi212[t] = N_Bi212[t-1] - decay_Bi212_Po212 - decay_Bi212_Tl208 + decay_Pb212_Bi212
    N_Pb212[t] = N_Pb212[t-1] - decay_Pb212_Bi212 + decay_Po216_Pb212
    N_Po216[t] = N_Po216[t-1] - decay_Po216_Pb212 + decay_Rn220_Po216
    N_Rn220[t] = N_Rn220[t-1] - decay_Rn220_Po216
    
    
#Plotting the data
plt.plot(time, N_Rn220, label="Radon 220")
plt.plot(time, N_Po216, label="Polonium 216")
plt.plot(time, N_Pb212, label="Lead 212")
plt.plot(time, N_Bi212, label="Bismuth 212")
plt.plot(time, N_Po212, label="Polonium 212")
plt.plot(time, N_Tl208, label="Thallium 208")
plt.plot(time, N_Pb208, label="Lead 208")
plt.xlabel("Time")
plt.ylabel("Number of Atoms")
plt.legend()
plt.show()



