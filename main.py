import random
import time
import pandas as pd
from datetime import datetime


def classify_aqi(value):

    if value <= 150:
        return "Good"

    elif value <= 300:
        return "Moderate"

    elif value <= 500:
        return "Poor"

    else:
        return "Hazardous"


print("=" * 50)
print("IoT Air Quality Monitoring Started")
print("=" * 50)

csv_file = "sensor_logs.csv"

while True:

    # Simulated Sensor Values
    air_quality = random.randint(
        100, 700
    )

    temperature = round(
        random.uniform(22, 40), 1
    )

    humidity = round(
        random.uniform(35, 85), 1
    )

    pollution_status = classify_aqi(
        air_quality
    )

    # Alert Logic
    if pollution_status in [
        "Poor",
        "Hazardous"
    ]:
        alert = "ALERT ON"

    else:
        alert = "SAFE"

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Save Data
    data = {
        "Timestamp": [timestamp],
        "Air Quality": [air_quality],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "Status": [pollution_status],
        "Alert": [alert]
    }

    df = pd.DataFrame(data)

    df.to_csv(
        csv_file,
        mode="a",
        header=not pd.io.common.file_exists(
            csv_file
        ),
        index=False
    )

    # Console Output
    print("\n====================")

    print(
        f"Timestamp: "
        f"{timestamp}"
    )

    print(
        f"Air Quality: "
        f"{air_quality}"
    )

    print(
        f"Temperature: "
        f"{temperature} °C"
    )

    print(
        f"Humidity: "
        f"{humidity} %"
    )

    print(
        f"Status: "
        f"{pollution_status}"
    )

    print(
        f"Alert: "
        f"{alert}"
    )

    print(
        "Saved to CSV"
    )

    time.sleep(3)