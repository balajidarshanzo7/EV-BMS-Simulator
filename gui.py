import tkinter as tk
from tkinter import ttk
from battery import Battery

battery = Battery()
is_charging = False
is_discharging = False

# Window setup
root = tk.Tk()
root.title("EV CAR DASHBOARD")
root.geometry("500x500")
root.configure(bg="black")
title = tk.Label(
    root,
    text="⚡ EV DASHBOARD ⚡",
    font=("Arial", 18, "bold"),
    fg="cyan",
    bg="black"
)
title.pack(pady=10)

# Labels
battery_label = tk.Label(
    root,
    text="Battery: 0%",
    font=("Arial", 20, "bold"),
    fg="lime",
    bg="black"
)
battery_label.pack(pady=10)
battery_bar = tk.Canvas(
    root,
    width=300,
    height=30,
    bg="black",
    highlightthickness=1
)

battery_bar.pack(pady=5)

battery_fill = battery_bar.create_rectangle(
    0, 0, 0, 30,
    fill="green"
)
battery_bar = ttk.Progressbar(
    root,
    orient="horizontal",
    length=250,
    mode="determinate"
)

battery_bar.pack(pady=10)

temp_label = tk.Label(root, text="Temp: 0°C", font=("Arial", 14))
temp_label.pack(pady=10)

voltage_label = tk.Label(root, text="Voltage: 0V", font=("Arial", 14))
voltage_label.pack(pady=10)

health_label = tk.Label(root, text="Health: 0%", font=("Arial", 14))
health_label.pack(pady=10)
range_label = tk.Label(root, text="Range: 0 km", font=("Arial", 14))
range_label.pack(pady=10)
charge_label = tk.Label(root, text="Charge Cycles: 0", font=("Arial", 12), fg="white", bg="black")
charge_label.pack(pady=5)

discharge_label = tk.Label(root, text="Discharge Cycles: 0", font=("Arial", 12), fg="white", bg="black")
discharge_label.pack(pady=5)
status_label = tk.Label(
    root,
    text="Status: NORMAL ✅",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="black"
)
prediction_label = tk.Label(
    root,
    text="Prediction: Healthy Battery",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="black"
)

prediction_label.pack(pady=5)

status_label.pack(pady=10)

def start_charge():
    global is_charging, is_discharging
    is_charging = True
    is_discharging = False

def start_discharge():
    global is_charging, is_discharging
    is_charging = False
    is_discharging = True

def stop_all():
    global is_charging, is_discharging
    is_charging = False
    is_discharging = False


btn1 = tk.Button(root, text="Charge ON", command=start_charge)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Discharge ON", command=start_discharge)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="STOP", command=stop_all)
btn3.pack(pady=5)



def update_ui():
    global is_charging, is_discharging

    # AUTO STOP at full charge
    if battery.battery_level >= 90:
        is_charging = False

    if is_charging:
        battery.charge()

    if is_discharging:
        battery.discharge()
    # Auto cooling system
    battery.cool_down()
    if battery.battery_level > 70:
        battery_label.config(fg="lime")

    elif battery.battery_level > 30:
        battery_label.config(fg="yellow")

    else:
        battery_label.config(fg="red")
    battery.read_esp32()
    battery.safety_check()
    battery.log_data()

    battery_label.config(text=f"Battery: {battery.battery_level}%")
    battery_bar["value"] = battery.battery_level
    battery_bar["value"] = battery.battery_level
    temp_label.config(text=f"Temp: {battery.temperature}°C")
    voltage_label.config(text=f"Voltage: {battery.voltage}V")
    health_label.config(text=f"Health: {battery.health}%")
    charge_label.config(text=f"Charge Cycles: {battery.charge_count}")
    discharge_label.config(text=f"Discharge Cycles: {battery.discharge_count}")
    range_label.config(
    text=f"Range: {battery.calculate_range():.1f} km"
)
    status_label.config(
    text=f"Status: {battery.get_status()}"
    
    )
    prediction_label.config(
    text=f"Prediction: {battery.predict_battery()}"
)
    status = battery.get_status()    

    if "NORMAL" in status:
        status_label.config(fg="lime")

    elif "WARNING" in status:
        status_label.config(fg="yellow")

    else:   
        status_label.config(fg="red")


    root.after(1000, update_ui)
    battery.log_data()
update_ui()
root.mainloop()