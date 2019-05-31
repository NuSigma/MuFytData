# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:08:11 2019

@author: Dylan Bailey
"""

import numpy as np
import matplotlib.pyplot as plt

from sympy import *

import tkinter as tk
from tkinter import filedialog

from scipy.optimize import least_squares



#IT WORKSSSSSSSSSS!!!!!!!!!!!!

"""
fcn = "A*cos(w*t)"

A, w, t = symbols('A w t')

expr = sympify(fcn)

f = lambdify([A, w, t], expr, "numpy")

print(f(1,2,3))
"""

#A little more advanced:

print('Input your function below: No assumed multiplication, type "help" for documentation.')
fcn = input("A(t) = ")

a0, w, t, phi, c, lmbda = symbols('a0 w t phi c lambda')

expr = sympify(fcn)
print(expr)

f = lambdify([a0, w, t, phi, c, lmbda], expr, "numpy")

timels=[6,5,6,7,8]
print(f(1,2,timels,4,5,6))
#output of the above for a0*cos(w*t+phi)+c
"""
a0*cos(phi + t*w) + c
[4.04234052 5.13673722 4.04234052 5.66031671 5.40808206]
"""