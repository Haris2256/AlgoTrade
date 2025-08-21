from openpyxl import load_workbook

file = "prices.xlsx"
stocks = load_workbook(file)

def buy_stock(stock, exchange, amount):
    sheet = stocks.worksheets[0]
    last_row = sheet.max_row + 1