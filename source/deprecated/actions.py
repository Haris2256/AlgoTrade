from datetime import datetime
import tkinter.messagebox as mb
import yfinance as yf

import variables

owned_sheet = variables.owned_sheet
transaction_sheet = variables.transaction_sheet
owned_header = variables.owned_header

date_format = variables.date_format

def validate(date, stock, price, amount):
    try:
        date = datetime.strptime(date, date_format).date()
    except ValueError:
        mb.showerror("Invalid Date", f"Please enter a valid date in DD-MMM-YY format. Got: {date}")
        return False
    # Parse Stock
    try:
        ticker = yf.Ticker(stock)
        info = ticker.fast_info
    except Exception:
        mb.showerror("Invalid Stock",f"This Stock is unknown: {stock}")
        return False
    # Parse Price
    try:
        price = float(price)
    except ValueError: 
        mb.showerror("Invalid Price", f"Please enter a number. Got: {price}")
        return False
    # Parse Amount
    try: 
        amount = float(amount)
    except ValueError:
        mb.showerror("Invalid Amount", f"Please enter a number. Got: {amount}")
        return False
    # Validate Price
    if price <= 0:
        mb.showerror("Invalid Price", f"Please enter a positive number. Got: {price}")
        return False
    # Validate Amount
    if amount <= 0:
        mb.showerror("Invalid Amount", f"Please enter a positive number. Got: {amount}")
        return False
    return (True, date, stock, price, amount)

def buy_stock(date, stock, price, amount):
    (valid, date, stock, price, amount) = validate(date, stock, price, amount)
    if not valid:
        return
    for row in range(2, owned_sheet.max_row + 1):
        if owned_sheet.cell(row=row, column=owned_header["name"]).value == stock:
            owned_sheet.cell(row=row, column=owned_header["amount"]).value += amount
            owned_sheet.cell(row=row, column=owned_header["book value"]).value += price * amount
            transaction_sheet.append([date, stock, "BUY", price, amount * price])
            return
    owned_sheet.append([stock, amount, amount * price])
    transaction_sheet.append([date, stock, "BUY", price, amount * price])

def sell_stock(date, stock, price, amount):
    (valid, date, stock, price, amount) = validate(date, stock, price, amount)
    if not valid:
        return
    for row in range(2, owned_sheet.max_row + 1):
        if owned_sheet.cell(row=row, column=owned_header["name"]).value == stock and owned_sheet.cell(row=row, column=2).value - amount >= 0:
            book_value = owned_sheet.cell(row=row, column=owned_header["book value"]).value
            owned_amount = owned_sheet.cell(row=row, column=owned_header["amount"]).value
            book_value -= amount * book_value / owned_amount
            owned_sheet.cell(row=row, column=owned_header["amount"]).value -= amount
            owned_sheet.cell(row=row, column=owned_header["book value"]).value = book_value
            transaction_sheet.append([date, stock, "SELL", price, amount * price])
            return

def stock_value(date, stock, price, value, action):
    try:
        num_price = float(price)
        num_value = float(value)
        action(date, stock, num_price, num_value / num_price)
    except ValueError:
        mb.showerror("Invalid Price or Amount", f"Please enter a number. Got: {num_price}, {num_value}")

