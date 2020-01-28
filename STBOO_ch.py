# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:03:49 2020

@author: Ben
"""

import numpy as np 
import matplotlib.pyplot as plt 

data = np.loadtxt('STBOOch_new.spectra_copy.txt',float)
spectrum = np.loadtxt('STBOO.spectrum_edited_ch.txt',float)

wavelength_real = spectrum[13:56,0]
flux_real = spectrum[16:59,1]

wavelength1 = data[58:249:,0]
flux1 = data[58:249,1]
wavelength2 = data[2648:2839,0]
flux2 = data[2648:2839,1]
wavelength3 = data[5238:5429,0]
flux3 = data[5238:5429,1]
wavelength4 = data[7828:8019,0]
flux4 = data[7828:8019,1]
wavelength5 = data[10418:10609,0]
flux5 = data[10418:10609,1]


plt.figure(figsize=(16,7))
#   Axes Labels
plt.xlabel('Wavelength ($\\AA$)')
plt.ylabel('Flux')

# Synthetic spectra plots
plt.plot(wavelength1,flux1, color=(0.6,0.6,0.6),  linestyle='-', label='[C/Fe] = 0.0 (Solar)')
plt.plot(wavelength2,flux2, color=(0.6,0.6,0.6), linestyle='--', label='[C/Fe] = 0.2')
plt.plot(wavelength3,flux3, color=(0.6,0.6,0.6), linestyle='-.', label = '[C/Fe] = 0.5')
plt.plot(wavelength4,flux4, color=(0.6,0.6,0.6), linestyle=':', label = '[C/Fe] = 0.8')
plt.plot(wavelength5,flux5, color=(0.6,0.6,0.6), linestyle='-', marker = '.', label = '[C/Fe] = 1.0 (10x Solar)')

# This is the actual data from STBOO
#plt.plot(wavelength_real,flux_real,color='black',marker="D",label='ST Bootes')
plt.scatter(wavelength_real, flux_real, color='black',marker = "D", label = 'ST Bootes')
plt.legend()
