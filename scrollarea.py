import tkinter as tk

def make_scrollarea(frame, colour): 
    container = tk.Frame(frame)         # holds both canvas and scrollbar
    container.pack(fill="both", expand=True)

    canvas = tk.Canvas(container, bg=colour, highlightthickness=0)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    # link canvas and scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # --- frame inside canvas where content goes ---
    content_frame = tk.Frame(canvas, bg=colour)

    # put that frame into the canvas
    window_id = canvas.create_window((0,0), window=content_frame, anchor="nw")

    # update scrollregion when widgets inside transaction_frame change size
    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", on_frame_configure)

    def on_canvas_configure(event):
        canvas.itemconfig(window_id, width=event.width)  # stretch to canvas width

    canvas.bind("<Configure>", on_canvas_configure)

    # Enable mousewheel scrolling
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)   # Windows/Mac
    canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux
    canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))   # Linux

    return content_frame