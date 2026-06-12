import pandas as pd
import matplotlib.pyplot as plt


# Load CSV file
df = pd.read_csv(
    "../sensor_logs.csv"
)

# Graph 1
plt.figure(figsize=(8, 5))

plt.plot(
    df["Air Quality"]
)

plt.title(
    "Air Quality Trend"
)

plt.xlabel(
    "Reading Number"
)

plt.ylabel(
    "Air Quality Value"
)

plt.grid(True)

plt.savefig(
    "air_quality_graph.png"
)

plt.show()


# Graph 2
plt.figure(figsize=(8, 5))

plt.plot(
    df["Temperature"]
)

plt.title(
    "Temperature Trend"
)

plt.xlabel(
    "Reading Number"
)

plt.ylabel(
    "Temperature °C"
)

plt.grid(True)

plt.savefig(
    "temperature_graph.png"
)

plt.show()


# Graph 3
plt.figure(figsize=(8, 5))

plt.plot(
    df["Humidity"]
)

plt.title(
    "Humidity Trend"
)

plt.xlabel(
    "Reading Number"
)

plt.ylabel(
    "Humidity %"
)

plt.grid(True)

plt.savefig(
    "humidity_graph.png"
)

plt.show()


print(
    "Graphs Generated Successfully!"
)