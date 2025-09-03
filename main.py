import tkinter as tk
import variables
import gui

root = tk.Tk()

gui.initialize_gui(root)

root.mainloop()

for row in range(variables.transaction_sheet.max_row, 1, -1):
        if variables.transaction_sheet.cell(row, 1).value is None:
            variables.transaction_sheet.delete_rows(row)

variables.stocks.save(variables.file)


