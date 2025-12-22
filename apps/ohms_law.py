import tkinter as tk

# Create main window
window = tk.Tk()
window.title("Ohm's Law Calculator")
window.geometry("420x300")   # Increased size
window.resizable(False, False)

# ---- Make window draggable ----
def start_move(event):
    window.x = event.x
    window.y = event.y

def stop_move(event):
    window.x = None
    window.y = None

def do_move(event):
    deltax = event.x - window.x
    deltay = event.y - window.y
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry(f"+{x}+{y}")

window.bind("<Button-1>", start_move)
window.bind("<ButtonRelease-1>", stop_move)
window.bind("<B1-Motion>", do_move)

# ---- Logic ----
def calculate_current():
    try:
        voltage = float(voltage_entry.get())
        resistance = float(resistance_entry.get())

        if resistance == 0:
            result_label.config(text="Resistance cannot be 0", fg="red")
            return

        current = voltage / resistance
        result_label.config(
            text=f"Current = {current:.3f} A",
            fg="green"
        )
    except:
        result_label.config(text="Invalid input", fg="red")

# ---- UI ----
title_label = tk.Label(
    window,
    text="Ohm's Law Calculator",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

input_frame = tk.Frame(window)
input_frame.pack()

tk.Label(input_frame, text="Voltage (V):", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5)
voltage_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
voltage_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Resistance (Ω):", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5)
resistance_entry = tk.Entry(input_frame, font=("Arial", 12), width=10)
resistance_entry.grid(row=1, column=1)

calc_button = tk.Button(
    window,
    text="Calculate Current",
    font=("Arial", 12),
    command=calculate_current
)
calc_button.pack(pady=15)

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=10)

# Start app
window.mainloop()
