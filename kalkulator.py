#!/usr/bin/env python3
"""
Kalkulator Lengkap Python
Fitur:
- Operasi dasar: +, -, *, /
- Operasi ilmiah: sin, cos, tan, log, ln, sqrt, factorial, power
- Persentase
- Riwayat
- GUI Tkinter + Mode Terminal (dua mode dalam satu file)

Jalankan:
    python kalkulator.py
    → pilih mode GUI atau Terminal
"""

import math
import sys
import tkinter as tk
from tkinter import ttk, messagebox

history = []

# =====================
#  LOGIC OPERATIONS
# =====================

def calculate_expression(expr: str):
    try:
        expr = expr.replace('^', '**')
        result = eval(expr, {
            '__builtins__': None,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'log': math.log10,
            'ln': math.log,
            'sqrt': math.sqrt,
            'pi': math.pi,
            'e': math.e,
            'fact': math.factorial
        })
        history.append((expr, result))
        return result
    except Exception as e:
        return f"Error: {e}"

# =====================
#  GUI MODE
# =====================

def run_gui():
    root = tk.Tk()
    root.title("Kalkulator Lengkap — Python")
    root.geometry("360x540")
    root.resizable(False, False)

    expr_var = tk.StringVar()

    entry = tk.Entry(root, textvariable=expr_var, font=("Arial", 20), justify='right')
    entry.pack(fill='x', padx=10, pady=10, ipady=10)

    def btn_click(value):
        expr_var.set(expr_var.get() + value)

    def clear():
        expr_var.set("")

    def compute():
        result = calculate_expression(expr_var.get())
        expr_var.set(str(result))

    buttons = [
        ['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['0', '.', '%', '+'],
        ['sin(', 'cos(', 'tan(', 'sqrt('],
        ['log(', 'ln(', 'fact(', 'pi'],
        ['(', ')', '^', '=']
    ]

    frame = tk.Frame(root)
    frame