import tkinter as tk

from source.deprecated import scrollarea, variables

transaction_sheet = variables.transaction_sheet
transaction_header = variables.transaction_header

owned_sheet = variables.owned_sheet
owned_header = variables.owned_header

main_panel_colour = variables.main_panel_colour
stock_label_colour = variables.stock_label_colour
text_colour = variables.text_colour

date_format = variables.date_format

tickers_dict = variables.tickers_dict
stocks_dict = {}

class Stock_Detail:
    def __init__(self, name, frame):
        self.name = name
        self.frame = frame
        self.amount = 0
        self.book_value = 0
        self.realized_return = 0
        self.unrealized_return = 0
        self.average_price = 0
        self.curr_price = tickers_dict[self.name].fast_info["last_price"]
        self.transactions = []
        self.name_lbl = tk.Label(self.frame,
                                    bg=stock_label_colour,
                                    fg=text_colour,
                                    text=self.name,
                                    font=("Poppins", 8))
        self.total_return_lbl = tk.Label(self.frame,
                                        bg=stock_label_colour,
                                        fg=text_colour,
                                        text="0",
                                        font=("Poppins", 8))
        self.unrealized_return_lbl = tk.Label(self.frame,
                                        bg=stock_label_colour,
                                        fg=text_colour,
                                        text="0",
                                        font=("Poppins", 8))
        self.realized_return_lbl = tk.Label(self.frame,
                                        bg=stock_label_colour,
                                        fg=text_colour,
                                        text="0",
                                        font=("Poppins", 8))
        self.average_price_lbl = tk.Label(self.frame,
                                    bg=stock_label_colour,
                                    text="0",
                                    fg=text_colour,
                                    font=("Poppins", 8))
        self.all_time_return_lbl = tk.Label(self.frame,
                                    bg=stock_label_colour,
                                    text="0",
                                    fg=text_colour,
                                    font=("Poppins", 8))
        self.percent_of_portfolio_return_lbl = tk.Label(self.frame,
                                    bg=stock_label_colour,
                                    text="0",
                                    fg=text_colour,
                                    font=("Poppins", 8))
    def add_transaction(self, row):
        date = transaction_sheet.cell(row, transaction_header["date"]).value
        name = transaction_sheet.cell(row, transaction_header["name"]).value
        action = transaction_sheet.cell(row, transaction_header["action"]).value
        price = transaction_sheet.cell(row, transaction_header["price"]).value
        value = transaction_sheet.cell(row, transaction_header["value"]).value
        self.transactions.append((date, name, action, price, value))
        if action == "BUY":
            self.amount += value / price
            self.book_value += value
        else:
            average_price = self.book_value / self.amount
            amount = value / price
            self.realized_return += (price - average_price) * amount
            self.book_value -= average_price * amount
            self.amount -= amount
        self.average_price = self.book_value / self.amount
        self.unrealized_return = (self.curr_price - self.average_price) * self.amount

    def configure_frame(self, portfolio_size):
        for i in range(7):
            self.frame.columnconfigure(i, weight=1, uniform="equal")
        self.frame.config(bg=stock_label_colour, padx=5, pady=5)
        # Name
        self.name_lbl.grid(row=0, column=0, sticky="ew")
        # Total Return
        total_return_value = self.realized_return + self.unrealized_return
        colorize_label(self.total_return_lbl, total_return_value, fmt="{:.2f}", prefix="$")
        self.total_return_lbl.grid(row=0, column=1, sticky="ew")

        # Unrealized Return
        colorize_label(self.unrealized_return_lbl, self.unrealized_return, fmt="{:.2f}", prefix="$")
        self.unrealized_return_lbl.grid(row=0, column=2, sticky="ew")

        # Realized Return
        colorize_label(self.realized_return_lbl, self.realized_return, fmt="{:.2f}", prefix="$")
        self.realized_return_lbl.grid(row=0, column=3, sticky="ew")

        # Average Price (doesn’t need colors, since it’s neutral)
        if self.amount == 0:
            self.average_price_lbl.config(text="0", fg=text_colour)
        else:
            self.average_price_lbl.config(text=f"${self.average_price:.2f}", fg=text_colour)
        self.average_price_lbl.grid(row=0, column=4, sticky="ew")

        # All-time Return (percentage)
        all_time_return_value = (self.curr_price / self.average_price - 1) * 100 if self.amount != 0 else 0
        colorize_label(self.all_time_return_lbl, all_time_return_value, fmt="{:.2f}", suffix="%")
        self.all_time_return_lbl.grid(row=0, column=5, sticky="ew")

        # Portfolio percentage
        self.percent_of_portfolio_return_lbl.config(text=f"{self.curr_price * self.amount / portfolio_size * 100:.2f}%", fg=text_colour)
        self.percent_of_portfolio_return_lbl.grid(row=0, column=6, sticky="ew")

def colorize_label(label, value, fmt="{:.2f}", prefix="", suffix="", neutral_color=text_colour):
    if value is None:
        label.config(text="N/A", fg=neutral_color)
    else:
        text = f"{prefix}{fmt.format(value)}{suffix}"
        label.config(
            text=text,
            fg="lightgreen" if value >= 0 else "red"
        )
def populate_overview_grid(frame, rows, label_bg, text_fg):
    for r, row in enumerate(rows):                # each row in the grid
        for c, (label_text, value) in enumerate(row):  # each (label,value) pair
            
            # Label (on the left side of each pair)
            tk.Label(
                frame,
                bg=label_bg,
                fg=text_fg,
                text=label_text,
                font=("Poppins", 14)
            ).grid(row=r, column=c*2, sticky="w")

            # Value (on the right side of each pair)
            if isinstance(value, (int, float)):
                formatted = f"${value:,.2f}"
                fg = "lightgreen" if value >= 0 else "red"
            else:
                formatted = str(value)
                fg = text_fg

            tk.Label(
                frame,
                bg=label_bg,
                fg=fg,
                text=formatted,
                font=("Poppins", 14)
            ).grid(row=r, column=c*2 + 1, padx=10, sticky="w")

def calculate_realized_return():
    sum = 0
    for detail in stocks_dict.values():
        sum += detail.realized_return
    return sum

def calculate_unrealized_return():
    sum = 0
    for detail in stocks_dict.values():
        sum += detail.unrealized_return
    return sum

def calculate_portfolio_size():
    sum = 0
    for detail in stocks_dict.values():
        sum += detail.curr_price * detail.amount
    return sum

def initialize_details(details_frame, main_frame):
    details_frame.pack(side="right", fill="both",expand=True)

    content_frame = scrollarea.make_scrollarea(details_frame, main_panel_colour)
    content_frame.pack(fill="both",expand=True)

    # Create Stock Objects:
    for row in range(2, transaction_sheet.max_row + 1):
        stock_name = transaction_sheet.cell(row, transaction_header["name"]).value

        # Ensure one Stock_Detail per name
        if stock_name not in stocks_dict:
            stock_info_frame = tk.Frame(content_frame)
            stocks_dict[stock_name] = Stock_Detail(stock_name, stock_info_frame)

        # Add transaction into that stock’s detail object
        stocks_dict[stock_name].add_transaction(row)

    # Exit button
    def on_exit():
        details_frame.destroy()
        stocks_dict.clear()
        main_frame.pack(side="right", fill="both", expand=True)

    exit_btn = tk.Button(
        content_frame, 
        text="Exit",
        command=on_exit, 
        font=("Poppins", 12),
        width=10
    )
    exit_btn.pack(anchor="w", padx=10, pady=10)

    # Overview
    overview_frame = tk.Frame(content_frame, bg=stock_label_colour)
    overview_frame.pack(fill="x", expand=True, anchor="n", padx=5, pady=10)

    total_realized_return = calculate_realized_return()
    total_unrealized_return = calculate_unrealized_return()
    total_return = total_realized_return + total_unrealized_return
    portfolio_size = calculate_portfolio_size()

    # Data to display
    overview_grid = [
        [("Total Return:", total_return), ("Realized Return:", total_realized_return)],
        [("Portfolio Value:", portfolio_size), ("Unrealized Return:", total_unrealized_return)]
    ]

    populate_overview_grid(
        overview_frame,
        overview_grid,
        label_bg=stock_label_colour,
        text_fg=text_colour
    )

    # Header
    header_frame = tk.Frame(content_frame, bg=stock_label_colour)
    header_frame.pack(fill="x", expand=True, anchor="n", padx=5, pady=10)
    headers = ["Name", "Total Return", "Unrealized", "Realized", "Average Price", "All-Time\nReturn", "Percent of\nPortfolio"]
    for i, name in enumerate(headers):
        header_frame.columnconfigure(i, weight=1, uniform="equal")
        tk.Label(
            header_frame,
            bg=stock_label_colour,
            fg=text_colour,
            text=name,
            font=("Poppins", 8)
        ).grid(row=0, column=i)
    
    # Stock Details
    for detail in stocks_dict.values():
        detail.configure_frame(portfolio_size)
        detail.frame.pack(fill="x", padx=5, pady=5, expand=True)




