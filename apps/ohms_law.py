# Ohm's Law Calculator
# I = V / R

voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ohms): "))

current = voltage / resistance

print("Current =", current, "A")
