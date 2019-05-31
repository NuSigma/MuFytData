# -*- coding: utf-8 -*-



import numpy as np
import sympy as sp
from sympy import sin, cos, exp
from scipy.optimize import least_squares
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


print('Welcome to MuFyt!\n')

inputExpr = input('Input fitting function: A(t) = ')
inputVars = input('List the parameters contained in the function above (comma separated): ')
inputVars = inputVars.split(',') # break the input into individual elements in a python list
inputVals = input('Provide starting guesses for each parameter (comma separated): ')
inputVals = list(map(float,inputVals.split(','))) # convert input to floats in a list



# open file dialog
root = tk.Tk()
root.withdraw()
fname = filedialog.askopenfilename()
# read in the data file from file dialog
texp, aexp, aerr, extra = np.loadtxt(fname,comments='%',delimiter=',',unpack=True)
# texp = time array from experimental data
# aexp = asymmetry array from experimental data
# aerr = experimental uncertainties on each data point
# extra = extra column not needed for this analysis


# create sympy symbols out of the variables provided by the user
symList = inputVars + ['t'] # add t to the list of variables
for entry in symList:
    sp.Symbol(entry) # convert each variable into a sympy symbol

# create sympy expression out of the equation provided by the user
symExpr = sp.sympify(inputExpr)
# convert the sympy expression to a form suitable for numerical evaluation
numExpr = sp.lambdify(symList,symExpr,"numpy")

# define the residual function for the fit
def residual(params,tArray,data,dataErr):
    calc = numExpr(*params,tArray)  #*params unpacks the params list into individual pieces
    return (data - calc)/dataErr**2

# perform the optimization using least_squares
optimized = least_squares(residual,inputVals,args=(texp,aexp,aerr))

# extract the refined values
fitVals = optimized.x

# display the refined values
print('Refined values:')
for idx, val in enumerate(fitVals):
    print(inputVars[idx]+' = '+str(val))

# display the fit
fit = numExpr(*fitVals,texp) #*fitvals unpacks list into individual pieces

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('t ($\mathdefault{\mu s}$)')
ax.set_ylabel('Asymmetry')
ax.errorbar(texp,aexp,yerr=aerr,marker='o',linestyle='None',color='b',zorder=1)
ax.plot(texp,fit,'r-',lw=2,zorder=2)

plt.tight_layout()
plt.show()
