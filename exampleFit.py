#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 13:10:00 2018

@author: dbbailey
"""

import numpy as np
import matplotlib.pyplot as plt
"""
datapath = input('\nEnter the Complete File Path for Data File: ')
t, a, da, c = np.loadtxt(datapath,comments='%',delimiter=',',
                         unpack=True)
"""
#Dialogue box file location
import tkinter as tk
from tkinter import filedialog

datapath = filedialog.askopenfilename()
        
t, a, da, c = np.loadtxt(datapath, comments='%', delimiter=',',unpack=True)


# a(t) = a0*cos(wt + phi) + c 
def func(p,x):
    a0,f,phi,c = p
    return a0*np.cos(2*np.pi*f*x+phi) + c

p0 = [0.23,0.45,0,0]
guess = func(p0, t)

from scipy.optimize import least_squares

def residual(p,x):
    return (a - func(p,x))/da**2

fit = least_squares(residual,p0,args=(t,))
pf = fit.x
print(pf)
bestfit = func(pf,t)


fig = plt.figure()
ax = fig.add_subplot(111)

ax.errorbar(t,a,yerr=da,marker='o',linestyle='none')
ax.plot(t,bestfit,'r-')

plt.show()