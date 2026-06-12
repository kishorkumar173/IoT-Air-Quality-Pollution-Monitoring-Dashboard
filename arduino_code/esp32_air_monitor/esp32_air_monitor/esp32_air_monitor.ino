#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11

#define LED_PIN 2
#define BUZZER_PIN 26

DHT dht(DHTPIN, DHTTYPE);

float temperature = 0;
float humidity = 0;

int airQuality = 0;
String pollutionStatus = "";

String classifyAQI(int value) {

  if (value <= 150) {
    return "Good";
  }

  else if (value <= 300) {
    return "Moderate";
  }

  else if (value <= 500) {
    return "Poor";
  }

  else {
    return "Hazardous";
  }
}

void setup() {

  Serial.begin(115200);

  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  dht.begin();

  Serial.println("IoT Air Quality Monitoring Started!");
}

void loop() {

  // Simulated Air Quality
  airQuality = random(100, 700);

  // DHT Sensor Reading
  temperature = dht.readTemperature();
  humidity = dht.readHumidity();

  pollutionStatus =
      classifyAQI(airQuality);

  // Alert Logic
  if (pollutionStatus == "Poor" ||
      pollutionStatus == "Hazardous") {

    digitalWrite(LED_PIN, HIGH);
    digitalWrite(BUZZER_PIN, HIGH);
  }

  else {

    digitalWrite(LED_PIN, LOW);
    digitalWrite(BUZZER_PIN, LOW);
  }

  // Serial Output
  Serial.println("====================");

  Serial.print("Air Quality: ");
  Serial.println(airQuality);

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  Serial.print("Status: ");
  Serial.println(pollutionStatus);

  delay(3000);
}