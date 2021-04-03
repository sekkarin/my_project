#include <Arduino.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

unsigned long previousMillis = 0; // will store last time LED was updated
// constants won't change:
const long interval = 432000; // 2 ชั่วโมง

int ldr = 13;
int soil_1 = 12;
int soil_2 = 13;

int rain_1 = 27;
int rain_2 = 26;
int rain_3 = 25;

int relay_light = 33;
int relay_low_temp = 32;

#define DHTPIN 23     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22 // DHT 22 (AM2302)

DHT_Unified dht(DHTPIN, DHTTYPE);

int read_temp();

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  dht.begin();
  pinMode(rain_1, INPUT);
  pinMode(rain_2, INPUT);
  pinMode(rain_3, INPUT);

  pinMode(relay_light, OUTPUT);
  pinMode(relay_low_temp, OUTPUT);
}

void loop()
{
  // put your main code here, to run repeatedly:
  // int get_value_1 = digitalRead(rain_1);
  // int get_value_2 = digitalRead(rain_2);
  // int get_value_3 = digitalRead(rain_3);
  // if ((get_value_1 && get_value_2 && get_value_3) == true)
  // {
  //   Serial.println("ฝนตก");
  //   Serial.println((digitalRead(rain_1) && digitalRead(rain_2) && digitalRead(rain_3)));
  //   delay(2000);
  // }
  // else
  // {
  //   Serial.println("ฝนไม่ตก");
  //   Serial.println((digitalRead(rain_1) && digitalRead(rain_2) && digitalRead(rain_3)));
  //   delay(2000);
  // }

  if (read_temp() > 27)
  {
    Serial.println(read_temp());
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval)
    {
      previousMillis = currentMillis;
      digitalWrite(relay_low_temp, HIGH);
    }
    //รดนํ้าเมื่ออุณหถูมิสูง
  }
  else
  {
    digitalWrite(relay_low_temp, LOW);
  }
  if (analogRead(ldr) <= 500)
  {
    // เงื่อนใขที่จะใส่
    digitalWrite(relay_light, HIGH);
  }
  else
  {
    digitalWrite(relay_light, LOW);
  }
  if (map(analogRead(soil_1), 0, 4096, 100, 0) < 20)
  {
    //เงื่อนใขที่ใส่
    delay(3000)
  }
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