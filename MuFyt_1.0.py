# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:43:17 2019

@author: Dylan Bailey
"""

#MuFyt Mk.4

import numpy as np
import matplotlib.pyplot as plt

from sympy import *

import tkinter as tk
from tkinter import filedialog

from scipy.optimize import least_squares



qtpr = False
while qtpr == False:
    print('Welcome to MuFyt!')
    
    upld = input('would you like to upload a file(y/n)? ')
    if upld.lower() == 'y':
        try:
            root = tk.Tk()
            root.withdraw()

            datapath = filedialog.askopenfilename()
        
            #Unpack data file into list variables:
            #Time - tm
            #the experimental value of the asymmetry - a
            #the statistical error on the value of each data point -er
            #Dr. Frandsen's Fit value -check value- chv
            tm, a, er, chv = np.loadtxt(datapath, comments='%', delimiter=','
                                ,unpack=True)

        #failed input
        except:
            #Quit Program
            if datapath.lower() == 'quit':
                qtpr = True
                break
            else:
                print('\nError: File Not Found or Incompatible File. '
                  + 'Check File Path and Try Again.\n\n')
                continue
            
            
        
        print('\nFile Successfully Imported.\n')
        gobk = False
        while gobk == False:
            print('\n\nPlease input a function below that you would like your data fitted to.')
            print('No assumed multiplication. Type "help" for understood variables,')
            print('constants, and function documentation.')
            print('or type "back" or "quit".\n')
            """
            potentially allow program to take user 
            defined variables and comments?
            """
            #Sympy Variable definitions:
            a0, w, t, ph, c, lmbda = symbols('a0 w t phi c lambda')
            
            fcn = input('\nA(t)= ')
            print('\n')
            #sanatize input?
            
            
            if fcn.lower() == 'quit':
                qtpr = True
                break
            
            elif fcn.lower() == 'back':
                gobk = True
                continue
            
            elif fcn.lower() == 'help':
                print('Documentation: \n')
                
            else:
                fld = True
                while fld == True:
                    try:
                        expr = sympify(fcn)
                        print(f'your chosen expression was: {expr}')
                
                        f = lambdify([a0, w, t, phi, c, lmbda], expr, "numpy")
                        
                    except:
                        #Deal with unusable input
                        print("\nError: Unknown Symbols or Functions Entered. "
                              + "Type 'Help' for Documentation and Please Try Again.\n")     
                        fld = True
                        continue
                    ph=10
                    fld = False
                #a and tm are lists from inputted files, assymetry and time respectively
                print(f(a, w, tm, ph, c, lmbda))
                #what value goes to w? phi? lmbda? c?
                #which are constants and which do we need  user input for?
                
                
                
                
    else:
        print('goodbye!')
        break
        