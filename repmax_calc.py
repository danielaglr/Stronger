import tkinter as tk
from tkinter import ttk
import sv_ttk
import math


def calculateLombardiOneRep(weight, reps):
  return round(weight * (reps ** 0.1))

def calculateLombardi(weight, reps, targetRep):
  return round(calculateLombardiOneRep(weight, reps) / targetRep ** 0.1)

def calculateEpleyOneRep(weight, reps):
  return round(weight * (1 + (reps / 30)))

def calculateEpley(weight, reps, targetRep):
  return round(calculateEpleyOneRep(weight, reps) / (1 + (targetRep / 30)))

def calculateAverageOneRep(weight, reps):
  return round((calculateLombardiOneRep(weight, reps) + calculateEpleyOneRep(weight, reps)) / 2)

def calculateAverage(weight, reps, targetRep):
  return round((calculateLombardi(weight, reps, targetRep) + calculateEpley(weight, reps, targetRep)) / 2)

def calculate_values():
  weight = int(weight_entry.get())
  reps = int(reps_entry.get())

  value_view.insert('', 0, values = (1, calculateAverageOneRep(weight, reps), calculateLombardiOneRep(weight, reps), calculateEpleyOneRep(weight, reps)))

  for x in range(2, 10):
    value_view.insert('', 'end', values = (x, calculateAverage(weight, reps, x), calculateLombardi(weight, reps, x), calculateEpley(weight, reps, x)))

root = tk.Tk()
root.title('Stronger | Analyzing Lifting Data and Making Predictions')

sv_ttk.set_theme('light')

frame = ttk.Frame(root)
frame.pack()

lifts_frame = ttk.LabelFrame(frame, text = 'Calculate One Rep Max')
lifts_frame.grid(row = 0, column = 0, padx = 10, pady = 20)

lift_entry = ttk.Entry(lifts_frame)
lift_entry.insert(0, "Lift Type")
lift_entry.bind("<FocusIn>", lambda e: lift_entry.delete('0', 'end'))
lift_entry.grid(row = 0, column = 0, padx = 5, pady = 10)

weight_entry = ttk.Entry(lifts_frame)
weight_entry.insert(0, "Weight")
weight_entry.bind("<FocusIn>", lambda e: weight_entry.delete('0', 'end'))
weight_entry.grid(row = 0, column = 1, padx = 5, pady = 10)

reps_entry = ttk.Entry(lifts_frame)
reps_entry.insert(0, "Reps")
reps_entry.bind("<FocusIn>", lambda e: reps_entry.delete('0', 'end'))
reps_entry.grid(row = 0, column = 2, padx = 5, pady = 10)

submit_button = ttk.Button(lifts_frame, text = "Calculate", command = lambda : calculate_values())
submit_button.grid(row = 0, column = 3, padx = 5, pady = 10)

module_separator = ttk.Separator(lifts_frame)
module_separator.grid(row = 1, column = 0)

values_frame = ttk.Frame(frame)
values_frame.grid(row = 1, column = 0)
values = ("Reps", "Average", "Lombardi", "Epley")

value_view = ttk.Treeview(values_frame, show = "headings", columns = values, height = 10)
value_view.column("Reps", width = 75)
value_view.column("Average", width = 150)
value_view.column("Lombardi", width = 150)
value_view.column("Epley", width = 150)

value_view.heading("Reps", text = "Reps")
value_view.heading("Average", text = "Average")
value_view.heading("Lombardi", text = "Lombardi")
value_view.heading("Epley", text = "Epley")

value_view.pack()

root.mainloop()