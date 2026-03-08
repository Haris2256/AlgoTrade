import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

container = tk.Frame(root)
container.pack(fill="both", expand=True)

canvas = tk.Canvas(container, bg="black")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

transaction_frame = tk.Frame(canvas, bg="gray")
window_id = canvas.create_window((0, 0), window=transaction_frame, anchor="nw")

def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

transaction_frame.bind("<Configure>", on_frame_configure)

def on_canvas_configure(event):
    canvas.itemconfig(window_id, width=event.width)  # stretch to canvas width

canvas.bind("<Configure>", on_canvas_configure)

# Add some rows
for r in range(10):
    row_frame = tk.Frame(transaction_frame, bg="white")
    row_frame.pack(fill="x")
    for c, txt in enumerate(["Name", "Action", "Price", "Value"]):
        row_frame.columnconfigure(c, weight=1, uniform="equal")
        lbl = tk.Label(row_frame, text=f"{txt} {r}", bg="lightblue")
        lbl.grid(row=0, column=c, sticky="nsew")

root.mainloop()