# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:09:28 2018

@author: Dylan Bailey
"""

import numpy as np
import matplotlib.pyplot as plt

from sympy import *
init_printing(use_unicode=True)

import tkinter as tk
from tkinter import filedialog

from scipy.optimize import least_squares


#Functions
def musr_constants():
    #Known Constants
    
    return

def func(p,fcn):
    #input file variables into chosen function
    #p is the desired input data, split into lists of a0, w, phi, and c
    #fcn is desired function
    #x is 
    a0, w, phi, c = p
       """How to eval function with lists of variables in SymPy???"""     
    
    return N(fcn)

def residual(p,x):
    #Residuals Calculation
    return (a - func(p,x))/da**2

def weigh_val():
    #Value Weighting Filter
    #Filters out values with residual of less than x and greater than y
    

#MAIN PROGRAM
print('\nWelcome to FytMuData\n')

quitprog = False
gobk = False


#Program Loop
while quitprog == False:
    try:
        root = tk.Tk()
        root.withdraw()

        datapath = filedialog.askopenfilename()
        
        #Unpack data file into list variables:
        #Time
        #the experimental value of the asymmetry
        #the statistical error on the value of each data point
        #and the calculated value based on a fit I performed 
        t, a, da, c = np.loadtxt(datapath, comments='%', delimiter=','
                                ,unpack=True)

        #failed input
    except:
                #Quit Program
        if datapath.lower() == 'quit':
            break
        else:
            print('\nError: File Not Found or Incompatible File. '
                  + 'Check File Path and Try Again.\n\n')
            continue
    
    print('\nSuccess!')
    
    
    while gobk == False:
        
        print("\n\nNow, select a function or input your own below." 
              + "\n1. a0*cos(wt + phi) + c" 
              + "\n2. a0*exp(-lmda*t)" 
              + "\n3. a0*sin(w*t+phi)/(w*t+phi)" 
              + "\n Type 'Help' for Syntax and Variable formatting, and Common Constants that are understood."
              + "\n or 'Back' to go back, or 'Quit' to quit the program. ")
        
        #Sympy Symbols Define:
        a0, w, t, phi, c = symbols('a0 w t phi c')
        
        fcn = input('a(t) = ')
            
        expr = 0
            
            
        print('\n') #Just Formatting
        
               
        #defining expresion 
        if fcn == '1':
            expr = a0*cos(w*t + phi) + c
            
        elif fcn == '2':
            expr = a0*cos(w*t+phi)
            
        elif fcn == '3':
            expr = a0*sin(w*t+phi)/(w*t+phi)
            
        elif fcn.lower() == 'help':
            #pertinant syntax SymPy documentation and accepted variables
            print("\nAccepted Variables and Common Constants: \n"
                  + "\n a0 = total amplitude of the asymmetry (i.e. the initial value at t=0)"
                  + "\n w = angular frequency of oscillation (equal to the muon gyromagnetic ratio times the magnetic field strength)"
                  + "\n t = time after implantation of the muon in the sample (typically measured in microseconds)"
                  + "\n lmda = lambda, exponential relaxation rate of the asymmetry due to spin fluctuations in the material and/or an inhomogeneous field distribution"
                  + "\n sig = gaussian relaxation rate of the asymmetry due to randomly oriented spins"
                  + "\n phi = phase offset of the muon spin oscillation due to precession during the muon flight path "
                  + "\n f = PLEASE CONVERT to w. frequency, w=2*pi*f  "  
                  + "\n c = up or down shift factor" 
                  
                  "\n\nFormatting Documentation: \n" 
                  + "\n ")
            
            #Return to file input    
            continue 
        
        elif fcn.lower() == 'back' or 'quit':
            if fcn.lower() == 'quit':
                quitprog = True
            
            break
                      
        else:
            expr = fcn
            """
            #Deal with unusable input???
            print("\nError: Unknown Symbols or Functions Entered. "
                  + "Type 'Help' for Documentation and Please Try Again.\n")     
            continue
            """
        
        #
        
        #Evaluate data in user Function
        
        


        
        
    
    
    