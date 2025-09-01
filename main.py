import tkinter as tk
import variables
import gui

root = tk.Tk()

gui.initialize_gui(root)

root.mainloop()

variables.stocks.save(variables.file)


