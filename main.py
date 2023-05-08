import tkinter as tk
from tkinter import ttk

import sv_ttk

root = tk.Tk()
root.title = 'Stronger | Analyzing Lifting Data and Making Predictions'

sv_ttk.set_theme('light')

frame = ttk.Frame(root)
frame.pack()

lifts_frame = ttk.LabelFrame(frame, text = 'Calculate One Rep Max')
lifts_frame.grid(row = 0, column = 0)

lift_entry = ttk.Entry(lifts_frame)
lift_entry.insert(0, "Lift Type")
lift_entry.bind("<FocusIn>", lambda e: lift_entry.delete('0', 'end'))
lift_entry.grid(row = 0, column = 0)

weight_entry = ttk.Entry(lifts_frame)
weight_entry.insert(0, "Weight")
weight_entry.bind("<FocusIn>", lambda e: weight_entry.delete('0', 'end'))
weight_entry.grid(row = 0, column = 1)

reps_entry = ttk.Entry(lifts_frame)
reps_entry.insert(0, "Reps")
reps_entry.bind("<FocusIn>", lambda e: reps_entry.delete('0', 'end'))
reps_entry.grid(row = 0, column = 2)

root.mainloop()