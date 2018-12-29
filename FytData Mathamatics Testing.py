# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 20:35:45 2018

@author: Dylan Bailey
"""

"""
FytData Mathamatics Testing
"""

"""
#Prof Frandsen's Program


#load file and unpack to variables
datapath = input('\nEnter the Complete File Path for Data File: ')
t, a, da, c = np.loadtxt(datapath,comments='%',delimiter=',',
                         unpack=True)


#function for setting up equation
# a(t) = a0*cos(w*t + phi) + c 
def func(p,x):
    a0,f,phi,c = p
    return a0*np.cos(2*np.pi*f*x+phi) + c


#function for residual
def residual(p,x):
    return (a - func(p,x))/da**2


#Guess Numbers plugged into function
p0 = [0.23,0.45,0,0]
guess = func(p0,t)


#Best fit
fit = least_squares(residual,p0,args=(t,))
pf = fit.x
print(pf)
bestfit = func(pf,t)


#graphing
fig = plt.figure()
ax = fig.add_subplot(111)


#Error plots
ax.errorbar(t,a,yerr=da,marker='o',linestyle='none')
ax.plot(t,bestfit,'r-')

plt.show()
"""


import numpy as np
import matplotlib.pyplot as plt

from sympy import *
import sympy
init_printing(use_unicode=True)

from scipy.optimize import least_squares

#Define Constants



#Define Potential Variables for Usage

sympy.var('a0 w t phi c')

fcninpt = input('Input custom Function: ')
func = sympify(fcninpt)


in1 = input('a0 = ')
in2 = input('\nw = ')
in3 = input('\nt = ')
in4 = input('\nphi = ')
in5 = input('\nc = ')


func = func.subs(a0,in1)
func = func.subs(w,in2)
func = func.subs(t,in3)
func = func.subs(phi,in4)
func = func.subs(c,in5)

func = simplify(func)
print(func) #Prints simplified expression with numbers...

#Next step to improve code: lambdify?
























