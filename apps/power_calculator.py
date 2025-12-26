import tkinter as tk

window = tk.Tk()
window.title("Power Calculator")
window.geometry("420x300")
window.resizable(False, False)

# for dragging
def start_move(event):
    window.x = event.x
    window.y = event.y

def do_move(event):
    x = window.winfo_x() + (event.x - window.x)
    y = window.winfo_y() + (event.y - window.y)
    window.geometry(f"+{x}+{y}")

window.bind("<Button-1>", start_move)
window.bind("<B1-Motion>", do_move)

# blah logic
def calculate_power():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        power = voltage * current
        result_label.config(text=f"Power = {power:.2f} W", fg="green")
    except:
        result_label.config(text="Invalid input", fg="red")

# UI
tk.Label(window, text="Power Calculator", font=("Arial", 18, "bold")).pack(pady=15)

frame = tk.Frame(window)
frame.pack()

tk.Label(frame, text="Voltage (V):", font=("Arial", 12)).grid(row=0, column=0, pady=5, padx=5)
voltage_entry = tk.Entry(frame, font=("Arial", 12), width=10)
voltage_entry.grid(row=0, column=1)

tk.Label(frame, text="Current (A):", font=("Arial", 12)).grid(row=1, column=0, pady=5, padx=5)
current_entry = tk.Entry(frame, font=("Arial", 12), width=10)
current_entry.grid(row=1, column=1)

tk.Button(
    window,
    text="Calculate Power",
    font=("Arial", 12),
    command=calculate_power
).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 20, "bold"))
result_label.pack(pady=10)

window.mainloop()
