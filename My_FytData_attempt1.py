#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 18:10:46 2018

@author: dbbailey
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares


print('Welcome to FytData\n\n')


def opnfl():
    """
    Input variables to load data into. t, a, da, c are reccomended.
    Format: t, a, da, c = opnfl()
    Function will unpack file inputted by user and return the filled variables.
    """
    datapath = input('\nEnter the Complete File Path for Data File: ')
     
    a, b, c, d = np.loadtxt(datapath, comments='%', delimiter=',',
                             unpack=True)
    return a, b, c, d


   
def funin():
    """
    Option to choose a mathematical function to use for fitting,
    or to input your own function. Outputs their decision
    """
    funout = input('Type in an option below. \n'
          '1. a(t) = a0*cos(wt + phi) + c\n'
          '2. so and so...\n'
          'Type Cancel to return to file selection.'
          '\n\nOr input your own function: a(t) = ')
    return funout
    
funcch = funin()    #funcch is function choice

if funcch.lower() == 'cancel':
    opnfl()
else:
      