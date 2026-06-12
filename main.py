import random
import time
<<<<<<< HEAD
=======
import requests
>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
import pandas as pd
from datetime import datetime


<<<<<<< HEAD
=======
# ThingSpeak Configuration
CHANNEL_ID = 3406483

WRITE_API_KEY = (
    "YOUR_WRITE_API_KEY"
)


>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
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

<<<<<<< HEAD
csv_file = "sensor_logs.csv"

while True:

    # Simulated Sensor Values
=======
csv_file = "../sensor_logs.csv"

while True:

    # Simulated Sensor Data
>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
    air_quality = random.randint(
        100, 700
    )

    temperature = round(
        random.uniform(22, 40), 1
    )

    humidity = round(
        random.uniform(35, 85), 1
    )

<<<<<<< HEAD
    pollution_status = classify_aqi(
        air_quality
    )

=======
    pollution_status = (
        classify_aqi(
            air_quality
        )
    )

    # Pollution Mapping
    status_map = {
        "Good": 1,
        "Moderate": 2,
        "Poor": 3,
        "Hazardous": 4
    }

    status_value = status_map[
        pollution_status
    ]

>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
    # Alert Logic
    if pollution_status in [
        "Poor",
        "Hazardous"
    ]:
<<<<<<< HEAD
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
=======

        alert = "ALERT ON"
        alert_value = 1

    else:

        alert = "SAFE"
        alert_value = 0

    timestamp = (
        datetime.now()
        .strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )

    # Save CSV
    data = {
        "Timestamp":
            [timestamp],

        "Air Quality":
            [air_quality],

        "Temperature":
            [temperature],

        "Humidity":
            [humidity],

        "Status":
            [pollution_status],

        "Alert":
            [alert]
>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
    }

    df = pd.DataFrame(data)

    df.to_csv(
        csv_file,
        mode="a",
<<<<<<< HEAD
        header=not pd.io.common.file_exists(
            csv_file
        ),
        index=False
    )

=======
        header=not pd.io.common
        .file_exists(csv_file),
        index=False
    )

    # Upload to ThingSpeak
    url = (
        "https://api.thingspeak.com/update"
    )

    payload = {
        "api_key":
            WRITE_API_KEY,

        "field1":
            air_quality,

        "field2":
            temperature,

        "field3":
            humidity,

        "field4":
            status_value,

        "field5":
            alert_value
    }

    response = requests.get(
        url,
        params=payload
    )

>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
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
<<<<<<< HEAD
        "Saved to CSV"
    )

    time.sleep(3)
=======
        "Uploaded to ThingSpeak!"
    )

    time.sleep(15)
>>>>>>> 1c12e860fdcaf202e10bb6a313e300c2abbdcd35
