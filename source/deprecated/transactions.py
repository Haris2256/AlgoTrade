import tkinter as tk
from datetime import datetime
import tkinter.messagebox as mb
from tkinter import ttk

import scrollarea
import variables

transaction_sheet = variables.transaction_sheet
transaction_header = variables.transaction_header

main_panel_colour = variables.main_panel_colour
stock_label_colour = variables.stock_label_colour
text_colour = variables.text_colour

date_format = variables.date_format

transactions = []

sort_options = ["Date", "Stock", "Action", "Price", "Value"]

class Transaction:
    def __init__(self, row, frame):
        self.row = row
        self.frame = frame
        self.frame.configure(bg=stock_label_colour, bd=1, relief="raised")
        for i in range(transaction_sheet.max_column):
            frame.columnconfigure(i, weight=1,uniform="equal")
        
        frame.pack(padx=5, pady=2, fill="x")
        # Values from the sheet
        self.date = transaction_sheet.cell(row, transaction_header["date"]).value
        if isinstance(self.date, datetime):
            self.date = self.date.date()
        self.name = transaction_sheet.cell(row, transaction_header["name"]).value
        self.action = transaction_sheet.cell(row, transaction_header["action"]).value
        self.price = transaction_sheet.cell(row, transaction_header["price"]).value
        self.value = transaction_sheet.cell(row, transaction_header["value"]).value

        # Labels
        self.name_lbl = tk.Label(frame, text=self.name, bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.action_lbl = tk.Label(frame, text=self.action, bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.price_lbl = tk.Label(frame, text=f"${self.price:.2f}", bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.value_lbl = tk.Label(frame, text=f"${self.value:.2f}", bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.date_lbl = tk.Label(frame, text=self.date.strftime(date_format), bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))

        # Pack Labels
        self.date_lbl.grid(row=0, column=0)
        self.name_lbl.grid(row=0, column=1)
        self.action_lbl.grid(row=0, column=2)
        self.price_lbl.grid(row=0, column=3)
        self.value_lbl.grid(row=0, column=4)

        # Entries for edit mode
        self.date_entry = tk.Entry(frame, bg=stock_label_colour, fg=text_colour,font=("Roboto", 12))
        self.name_entry = tk.Entry(frame, bg=stock_label_colour, fg=text_colour,font=("Roboto", 12))
        self.action_entry = tk.Entry(frame, bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.price_entry = tk.Entry(frame, bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))
        self.value_entry = tk.Entry(frame, bg=stock_label_colour, fg=text_colour, font=("Roboto", 12))

        # Pre-fill entries with current values
        self.date_entry.insert(0, self.date.strftime(date_format))
        self.name_entry.insert(0, self.name)
        self.action_entry.insert(0, self.action)
        self.price_entry.insert(0, self.price)
        self.value_entry.insert(0, self.value)

        # Delete Button
        self.del_btn = tk.Button(frame, bg=stock_label_colour, fg=text_colour, text="X", command=self.delete)
    
    def convert_edit(self):
        self.name_lbl.grid_forget()
        self.action_lbl.grid_forget()
        self.price_lbl.grid_forget()
        self.value_lbl.grid_forget()
        self.date_lbl.grid_forget()

        self.date_entry.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.action_entry.grid(row=0, column=2)
        self.price_entry.grid(row=0, column=3)
        self.value_entry.grid(row=0, column=4)

        self.del_btn.grid(row=0, column=5)

    def save(self):
        new_name = self.name_entry.get()
        new_action = self.action_entry.get().upper()
        if new_action != "BUY" and new_action != "SELL":
            mb.showerror("Invalid Action", f"Please enter BUY or SELL. Got: {new_action}")
            new_action = self.action
        try:
            new_date = self.date_entry.get()
            new_date = datetime.strptime(new_date, date_format).date()
        except (ValueError, TypeError):
            mb.showerror("Invalid Date", f"Please enter date as YYYY-MM-DD. Got: {new_date}")
            new_date = self.date
        try:
            new_price = self.price_entry.get()
            new_price = float(new_price)
        except (ValueError, TypeError):
            mb.showerror("Invalid Price", f"Please enter a number for price. Got: {new_price}")
            new_price = self.price
        try:
            new_value = self.value_entry.get()
            new_value  = float(new_value)
        except (ValueError, TypeError):
            mb.showerror("Invalid Value", f"Please enter a number for value. Got: {new_value}")
            new_value = self.value

        transaction_sheet.cell(self.row, transaction_header["date"]).value = new_date
        transaction_sheet.cell(self.row, transaction_header["name"]).value = new_name
        transaction_sheet.cell(self.row, transaction_header["action"]).value = new_action
        transaction_sheet.cell(self.row, transaction_header["price"]).value = new_price
        transaction_sheet.cell(self.row, transaction_header["value"]).value = new_value

        self.date, self.name, self.action, self.price, self.value = new_date, new_name, new_action, new_price, new_value

        self.date_lbl.config(text=new_date.strftime(date_format))
        self.name_lbl.config(text=new_name)
        self.action_lbl.config(text=new_action)
        self.price_lbl.config(text=f"${new_price:.2f}")
        self.value_lbl.config(text=f"${new_value:.2f}")

        self.date_entry.grid_forget()
        self.name_entry.grid_forget()
        self.action_entry.grid_forget()
        self.price_entry.grid_forget()
        self.value_entry.grid_forget()

        self.del_btn.grid_forget()

        self.date_lbl.grid(row=0, column=0)
        self.name_lbl.grid(row=0, column=1)
        self.action_lbl.grid(row=0, column=2)
        self.price_lbl.grid(row=0, column=3)
        self.value_lbl.grid(row=0, column=4)
    
    def delete(self):
        transactions.remove(self)
        clear_row(transaction_sheet, self.row)
        self.frame.destroy()

def clear_row(sheet, row):
    sheet.cell(row=row, column=1).value = None

def collapse_empty_rows(sheet):
    for row in range(sheet.max_row, 1, -1):
        if sheet.cell(row, 1).value is None:
            sheet.delete_rows(row)

def sort_transactions(by="date", reverse=False):
    key_funcs = {
        "date": lambda t: t.date,
        "stock": lambda t: t.name,
        "action": lambda t: t.action,
        "price": lambda t: t.price,
        "amount": lambda t: t.amount,
        "value": lambda t: t.value,
    }
    if by not in key_funcs:
        return
    
    # sort in place
    transactions.sort(key=key_funcs[by], reverse=reverse)
    # re-display
    refresh_transaction_gui()

def refresh_transaction_gui():
    for transaction in transactions:
        transaction.frame.pack_forget()
        transaction.frame.pack(padx=5, pady=2, fill="x")


def initialize_transactions(transaction_frame, main_frame):
    button_frame = tk.Frame(transaction_frame, bg=main_panel_colour)
    button_frame.pack(fill="x")

    # Exit Button
    def on_exit():
        transaction_frame.destroy()
        transactions.clear()
        collapse_empty_rows(transaction_sheet)
        main_frame.pack(side="right", fill="both", expand=True)

    exit_btn = tk.Button(
        button_frame, 
        text="Exit",
        command=on_exit, 
        font=("Poppins", 12),
        width=10
    )
    exit_btn.pack(side="left", anchor="n",pady=10, padx=10)

    def on_edit():
        for transaction in transactions:
            transaction.convert_edit()
    edit_btn = tk.Button(
        button_frame, 
        text="Edit", 
        command=on_edit, 
        font=("Poppins", 12),
        width=10
    )
    edit_btn.pack(side="right", anchor="n",pady=10, padx=10)

    def on_save():
        for transaction in transactions:
            transaction.save()
    save_btn = tk.Button(
        button_frame, 
        text="Save", 
        command=on_save, 
        font=("Poppins", 12),
        width=10
    )
    save_btn.pack(side="right", anchor="n",pady=10, padx=10)

    def on_sort_change(event=None):
        choice = selected_sort.get().lower()
        sort_transactions(choice, reverse=reverse_sort.get())
        sort_menu.selection_clear()

    reverse_sort = tk.BooleanVar(value=False)  # Default unchecked (ascending)
    reverse_check = tk.Checkbutton(
        button_frame,
        bg=main_panel_colour,             # background of the whole widget
        fg=text_colour,                   # label + checkmark color
        activebackground=main_panel_colour,
        activeforeground=text_colour,
        selectcolor=main_panel_colour,
        text="Reverse",
        variable=reverse_sort,
        command=on_sort_change,
        font=("Poppins", 12),
        onvalue=True,
        offvalue=False
    )
    reverse_check.pack(pady=10, padx=10, side="right")

    # Sort Options
    selected_sort = tk.StringVar()
    sort_menu = ttk.Combobox(
        button_frame, 
        textvariable=selected_sort, 
        values=sort_options, 
        state="readonly", 
        font=("Poppins", 12), 
        width=6
    )
    sort_menu.current(0)
    sort_menu.pack(pady=10, padx=10, side="right", fill="y")
    sort_menu.bind("<<ComboboxSelected>>", on_sort_change)

    # List of transactions
    content_frame = scrollarea.make_scrollarea(transaction_frame, main_panel_colour)
    header_frame = tk.Frame(content_frame, bg=stock_label_colour, bd=1, relief="raised")
    header_frame.pack(fill="x", padx=5, pady=10)
    for i in range(1,transaction_sheet.max_column + 1):
        header_frame.columnconfigure(i, weight=1, uniform="equal")
        name = transaction_sheet.cell(1, i).value
        name = name.upper()
        label = tk.Label(
            header_frame, 
            bg=stock_label_colour, 
            fg=text_colour,
            text=name, 
            font=("Roboto", 12)
        )
        label.grid(row=0,column=i, sticky="ew")

    # Transaction rows
    for row in range(2, transaction_sheet.max_row + 1):
        frame = tk.Frame(content_frame)
        transaction = Transaction(row, frame)
        transactions.append(transaction)


