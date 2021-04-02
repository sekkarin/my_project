#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

int ldr = 13;
int soil_1 = 12;
int rain_1 = 27;

#define DHTPIN 23     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22 // DHT 22 (AM2302)

DHT_Unified dht(DHTPIN, DHTTYPE);

int read_ldr();
int read_soil(int pin); //2 ตัว
int read_rain(int pin); // 3 ตัว
int read_temp();

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  dht.begin();
  pinMode(rain_1, INPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  Serial.println(read_temp());
}

int read_ldr()
{
  return analogRead(ldr);
}
int read_soil(int pin)
{
  return analogRead(pin);
}
int read_rain(int pin)
{
  return digitalRead(pin);
}
int read_temp()
{

  sensors_event_t event;
  delay(200);
  dht.temperature().getEvent(&event);
  if (isnan(event.temperature))
  {
    Serial.println(F("Error reading temperature!"));
  }
  else
  {
    return event.temperature;
  }
}