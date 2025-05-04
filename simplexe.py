# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:05:17 2025

@author: jujub
"""

import os
import tkinter as tk
from tkinter import ttk
import numpy as np
from fractions import Fraction

class Matrix:
    def __init__(self, values:np.array):
        self.rows, self.cols = values.shape
        self.values = values

class SimplexTable:
    def __init__(self, constraints, variables, costs, value, values):
        self.constraints = constraints
        self.variables = variables
        self.costs = costs
        self.value = value
        self.values = values

basedir = os.path.dirname(__file__)

menu = tk.Tk()
menu.title("Solveur du simplexe")
menu.geometry("350x100")
menu.iconbitmap(os.path.join(basedir, "icon.ico"))

#list of options available to the user
options = ["Choisir l'option désirée", "Effectuer un pivot", "Standardiser un problème"]

#variable to store the number of constraints in the problem
constraints = tk.StringVar(value="1")

#variable to store the number of variables in the problem
variables = tk.StringVar(value="1")

def open_pivot_menu():
    pivot_menu_window = tk.Toplevel()
    pivot_menu_window.title("Pivoteur du simplexe")
    #pivot_menu_window.geometry("400x200")
    pivot_menu_window.iconbitmap(os.path.join(basedir, "icon.ico"))

    pivot_menu_label_constraints = tk.Label(pivot_menu_window, text="Nombre de contraintes")
    pivot_menu_spinbox_constraints = tk.Spinbox(pivot_menu_window, from_=1, to=10, textvariable=constraints)
    pivot_menu_label_variables = tk.Label(pivot_menu_window, text="Nombre de variables")
    pivot_menu_spinbox_variables = tk.Spinbox(pivot_menu_window, from_=1, to=10, textvariable=variables)
    pivot_menu_button = tk.Button(pivot_menu_window, text="Go!")

    pivot_menu_label_constraints.grid(row=0, column=0, padx=5, pady=5)
    pivot_menu_spinbox_constraints.grid(row=0, column=1, padx=5, pady=5)
    pivot_menu_label_variables.grid(row=1, column=0, padx=5, pady=5)
    pivot_menu_spinbox_variables.grid(row=1, column=1, padx=5, pady=5)
    pivot_menu_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="esnw")

def open_std_menu():
    std_menu_window = tk.Toplevel()
    std_menu_window.title("Standardisateur du simplexe")
    std_menu_window.geometry("500x300")
    std_menu_window.iconbitmap(os.path.join(basedir, "icon.ico"))

def handle_menu_button_press(event):
    if (menu_cbox.get() == options[0]):
        pass
    elif (menu_cbox.get() == options[1]):
        open_pivot_menu()
    elif (menu_cbox.get() == options[2]):
        open_std_menu()

#initialize a combo box with the options of what the app can do for the user
menu_cbox = ttk.Combobox(menu, values=options)
menu_cbox.set(options[0])
menu_cbox.pack(padx=10, pady=10, fill="x")

#make a button that will send the user to the desired window
menu_button = tk.Button(menu, text="Go!")
menu_button.bind("<Button-1>", handle_menu_button_press, "+")
menu_button.pack(padx=10, pady=10)

menu.mainloop()
