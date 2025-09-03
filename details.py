import tkinter as tk
from openpyxl import load_workbook
from datetime import datetime
import tkinter.messagebox as mb
from tkinter import ttk

import variables

transaction_sheet = variables.transaction_sheet
transaction_header = variables.transaction_header

main_panel_colour = variables.main_panel_colour
stock_label_colour = variables.stock_label_colour
text_colour = variables.text_colour

date_format = variables.date_format

transactions = []

