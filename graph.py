import pandas as pd
import matplotlib.pyplot as plt

# CSV read
data = pd.read_csv(
    "battery_log.csv",
    header=None,
    names=["Battery", "Temperature", "Voltage", "Health"]
)

# Graph
plt.plot(data["Battery"])

plt.title("Battery Level vs Time")
plt.xlabel("Time")
plt.ylabel("Battery Percentage")

plt.show()