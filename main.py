from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(fahrenheit.get())
        celsius.set(int(value - 32) * 5 / 9)
    except ValueError:
        pass


root = Tk()
root.title("Fahrenheit to Celsius")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

fahrenheit = StringVar()
fahrenheit_entry = ttk.Entry(mainframe, width=7, textvariable=fahrenheit)
fahrenheit_entry.grid(column=2, row=1, sticky=(W, E))

celsius = StringVar()
ttk.Label(mainframe, textvariable=celsius).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="Fahrenheit").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Celsius").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

fahrenheit_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
