import csv
import serial
class Battery:
    def __init__(self):
        self.battery_level = 70
        self.temperature = 30
        self.voltage = 3.7
        self.health = 100

        self.charge_count = 0
        self.discharge_count = 0

        try:
            self.ser = serial.Serial("COM5", 115200, timeout=1)
        except:
            self.ser = None

        self.charge_count = 0
        self.discharge_count = 0

    def charge(self):
        if self.battery_level < 100:
            self.battery_level += 10
            self.temperature += 1
            self.voltage += 0.05
            self.health -= 0.1
            self.charge_count += 1

        if self.battery_level > 100:
            self.battery_level = 100

    def discharge(self):
        if self.battery_level > 0:
            self.battery_level -= 5
            self.temperature += 0.5
            self.voltage -= 0.03
            self.health -= 0.05
            self.discharge_count += 1

        if self.battery_level < 0:
            self.battery_level = 0

    def check_temperature(self):
        if self.temperature > 45:
            print("⚠ WARNING: Battery Overheating!")

    def safety_check(self):
        if self.battery_level >= 90:
            print("⚠ Battery Full - Auto Stop Charging")

        if self.temperature > 45:
            print("🔥 Overheat Detected - Cooling Mode ON")

        if self.health < 50:
            print("⚠ Warning: Battery Health Low")

    def cool_down(self):
        if self.temperature > 35:
            self.temperature -= 0.5

    def calculate_range(self):
        return (self.battery_level / 100) * 300

    def get_status(self):
        if self.temperature > 55:
            return "CRITICAL 🔥"
        elif self.temperature > 45 or self.health < 50:
            return "WARNING ⚠️"
        else:
            return "NORMAL ✅"
    def predict_battery(self):
        if self.health >= 80:
            return "🟢 Healthy Battery"

        elif self.health >= 60:
            return "🟡 Battery Aging Detected"

        else:
            return "🔴 Battery Replacement Recommended"
    def read_esp32(self):
        if self.ser is None:
            return

        try:
            line = self.ser.readline().decode().strip()

            print(line)
            if "Battery Voltage:" in line:
                parts = line.split("|")
                voltage = float(
                    parts[0]
                    .replace("Battery Voltage:", "")
                    .replace("V", "")
                    .strip()
                )

                temperature = float(
                    parts[1]
                    .replace("Temperature:", "")
                    .replace("C", "")
                    .strip()
                )

                self.voltage = round(voltage, 2)
                if self.voltage < 3.0 or self.voltage > 4.3:
                    self.voltage = 3.7
                if temperature <= 0:
                    self.temperature = 30
                else:
                    self.temperature = round(temperature, 2)

                percent = 100

                if percent > 100:
                    percent = 100

                if percent < 0:
                    percent = 0

                self.battery_level = round(percent)

        except Exception as e:
            print("ESP32 Error:", e)

    def log_data(self):
        with open("battery_log.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
            self.battery_level,
            self.temperature,
            self.voltage,
            self.health
        ])