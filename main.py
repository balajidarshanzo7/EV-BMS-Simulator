from battery import Battery

battery = Battery()

print("Initial Status:")
print("Battery:", battery.battery_level, "%")
print("Temp:", battery.temperature, "°C")
print("Voltage:", battery.voltage, "V")
print("Health:", battery.health, "%")

print("\nCharging...")
battery.charge()
battery.check_temperature()

print("After Charge:")
print("Battery:", battery.battery_level, "%")
print("Temp:", battery.temperature, "°C")
print("Voltage:", battery.voltage, "V")

print("\nDischarging...")
battery.discharge()
battery.check_temperature()
print("After Discharge:")
print("Battery:", battery.battery_level, "%")
print("Temp:", battery.temperature, "°C")
print("Voltage:", battery.voltage, "V")