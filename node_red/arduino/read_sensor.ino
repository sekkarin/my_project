

#include "DHT.h"
#include <Arduino_JSON.h>
#define DHTPIN D2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11 // DHT 11
DHT dht(DHTPIN, DHTTYPE);
JSONVar json_value;
//raed LRD PIN
int ldr = A0;

void setup()
{
  Serial.begin(115200);
  Serial.println(F("DHTxx test!"));
  dht.begin();
}

void loop()
{
  int value = map(analogRead(ldr), 0, 1024, 0, 100);
  //อ่านค่า LDR และ ปริ้นออกมา
  Serial.println(value);


  int h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  int t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  int f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f))
  {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  // Compute heat index in Fahrenheit (the default)
  int hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  int hic = dht.computeHeatIndex(t, h, false);

  json_value["data_sensor"]["Humidity"] = h;
  json_value["data_sensor"]["Temperature"] = t;
  json_value["data_sensor"]["Heat_index"] = hic;
  json_value["data_sensor"]["ldr"] = value;
  Serial.println(json_value);
  delay(2000);
  // Wait a few seconds between measurements.
}
