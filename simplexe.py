# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:05:17 2025

@author: jujub
"""

from tkinter import *
from tkinter import ttk
import numpy as np
from fractions import Fraction

class Matrix:
    def __init__(self, values):
        self.rows, self.cols = values.shape
        self.values = values

class SimplexTable:
    def __init__(self, constraints, variables, costs, value, values):
        self.constraints = constraints
        self.variables = variables
        self.costs = costs
        self.value = value
        self.values = values

menu = Tk()
menu.title("Pivoteur du Simplexe")

frm = ttk.Frame(menu, padding=10)
frm.grid()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=menu.destroy).grid(column=1, row=1)

menu.mainloop()
