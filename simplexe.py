# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:05:17 2025

@author: jujub
"""

from tkinter import *
from tkinter import ttk
import numpy as np

class Matrix:
    def __init__(self, rows, cols, values):
        self.rows = rows
        self.cols = cols
        if (values.size < rows*cols): raise ValueError("Pas assez de valeurs pour initialiser la matrice.")
        if (values.size > rows*cols): raise ValueError("Trop de valeurs pour initialiser la matrice.")
        self.values = values
        

class SimplexTable:
    def __init__(self, constraints, variables, costs, value, values):
        self.constraints = constraints

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
