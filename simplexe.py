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

basedir = os.path.dirname(__file__)

menu_window = tk.Tk()
menu_window.title("Solveur du simplexe")
menu_window.geometry("350x100")
menu_window.iconbitmap(os.path.join(basedir, "icon.ico"))

#list of options available to the user
options = ["Choisir l'option désirée", "Effectuer un pivot", "Standardiser un problème"]

#variable to store the number of constraints in the problem
constraints = tk.StringVar(value="1")

#variable to store the number of variables in the problem
variables = tk.StringVar(value="1")

#variable to store the names of the variables in the problem
var_names = []

#variables to store the bases when doing the pivot
init_base = []
new_base = []

def error_window(msg):
    err_win = tk.Toplevel()
    err_win.title("Erreur")
    err_win.iconbitmap(os.path.join(basedir, "icon.ico"))

    err_lbl = tk.Label(err_win, text=msg)
    err_lbl.pack(padx=5, pady=5, fill="x")

    err_btn = tk.Button(err_win, text="OK", command=err_win.destroy)
    err_btn.pack(padx=5, pady=5)

def open_pivot_window():
    pivot_window = tk.Toplevel()
    pivot_window.title("Pivoteur du simplexe")
    pivot_window.iconbitmap(os.path.join(basedir, "icon.ico"))

    global pivot_window_elements
    pivot_window_elements = []
    element_row = []

    element_row.append(tk.Label(pivot_window, text="Base initiale"))
    element_row.append(tk.Label(pivot_window, text="Nouvelle base"))
    for j in range(int(variables.get())):
        element_row.append(tk.Entry(pivot_window))
        element_row[-1].insert(0, f"var{j+1}")
    element_row.append(tk.Label(pivot_window, text="TDD"))
    pivot_window_elements.append(element_row)
    element_row = []

    for i in range(int(constraints.get())):
        element_row.append(tk.Entry(pivot_window))
        element_row.append(tk.Entry(pivot_window))
        for j in range(int(variables.get())):
            element_row.append(tk.Entry(pivot_window))
        element_row.append(tk.Entry(pivot_window))
        pivot_window_elements.append(element_row)
        element_row = []

    element_row.append(tk.Label(pivot_window, text=""))
    element_row.append(tk.Label(pivot_window, text="-Z"))
    for j in range(int(variables.get())):
        element_row.append(tk.Entry(pivot_window))
    element_row.append(tk.Entry(pivot_window))
    pivot_window_elements.append(element_row)

    execute_pivot_button = tk.Button(pivot_window, text="Effectuer le pivot", command=execute_pivot)

    for i in range(len(pivot_window_elements)):
        for j in range(len(element_row)):
            pivot_window_elements[i][j].grid(row=i, column=j, padx=5, pady=5)

    execute_pivot_button.grid(row=len(pivot_window_elements), column=len(element_row), padx=5, pady=5)

def execute_pivot():
#make sure that all vaiables have different names
    var_names = []
    for i in range(int(variables.get())):
        var_names.append(pivot_window_elements[0][i+2].get())
    if (len(var_names) != len(set(var_names))):
        error_window("Les variables doivent avoir des noms uniques.")
        return

#make sure all base variables have different names and are part of the problem variables
    init_base = []
    new_base = []
    try:
        for i in range(int(constraints.get())):
            init_base.append(var_names.index(pivot_window_elements[i+1][0].get()))
            new_base.append(var_names.index(pivot_window_elements[i+1][1].get()))
    except ValueError:
        error_window("Les variables de bases doivent être des variables du problème.")
        return
    if (len(init_base) != len(set(init_base)) or len(new_base) != len(set(new_base))):
        error_window("Les variables de bases doivent être uniques.")
        return

    error_window(str(var_names))

def open_pivot_menu():
    pivot_menu_window = tk.Toplevel()
    pivot_menu_window.title("Pivoteur du simplexe")
    pivot_menu_window.iconbitmap(os.path.join(basedir, "icon.ico"))

    pivot_menu_label_constraints = tk.Label(pivot_menu_window, text="Nombre de contraintes")
    pivot_menu_spinbox_constraints = tk.Spinbox(pivot_menu_window, from_=1, to=10, textvariable=constraints)
    pivot_menu_label_variables = tk.Label(pivot_menu_window, text="Nombre de variables")
    pivot_menu_spinbox_variables = tk.Spinbox(pivot_menu_window, from_=1, to=10, textvariable=variables)
    pivot_menu_button = tk.Button(pivot_menu_window, text="Go!", command=open_pivot_window)

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

def handle_menu_button_press():
    if (menu_cbox.get() == options[0]):
        pass
    elif (menu_cbox.get() == options[1]):
        open_pivot_menu()
    elif (menu_cbox.get() == options[2]):
        open_std_menu()

#initialize a combo box with the options of what the app can do for the user
menu_cbox = ttk.Combobox(menu_window, values=options)
menu_cbox.set(options[0])
menu_cbox.pack(padx=10, pady=10, fill="x")

#make a button that will send the user to the desired window
menu_button = tk.Button(menu_window, text="Go!", command=handle_menu_button_press)
menu_button.pack(padx=10, pady=10)

menu_window.mainloop()
