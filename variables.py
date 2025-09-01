from openpyxl import load_workbook

file = "stocks.xlsx"
stocks = load_workbook(file)

owned_sheet = stocks["owned stocks"]
watchlist_sheet = stocks["watchlist"]
transaction_sheet = stocks["transactions"]

owned_header = {cell.value: idx for idx, cell in enumerate(owned_sheet[1], start=1)}
transaction_header = {cell.value: idx for idx, cell in enumerate(transaction_sheet[1], start=1)}

# Colours
side_colour = "#363636"
main_panel_colour = "#1F1F1F"
stock_label_colour = "#2A2A2A"
text_colour = "#EEEEEE"

# Watchlist Configuration
num_stocks_per_row = 5
num_stocks_per_column = 5