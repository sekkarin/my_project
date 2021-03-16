#include <ESP8266WiFi.h>
#include <FirebaseESP8266.h>

#define FIREBASE_HOST "iot-begin-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "RYAjDY3D1laUkUhk5HmMqVUSy3g61GNOor4wUuL4"
#define WIFI_SSID "microchip"
#define WIFI_PASSWORD "12345678"

//Define FirebaseESP8266 data object
FirebaseData fbdo;
int dustPin = A0;
int ledPower = D2;
int delayTime = 280;
int delayTime2 = 40;
float offTime = 9680;

unsigned long previousMillis = 0;
const long interval = 1000;

String path = "/dust";
int Detecting_of_dust();
void setup()
{
  pinMode(ledPower, OUTPUT);
  pinMode(4, OUTPUT);

  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED)
  {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
}

void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval)
  {
    // save the last time you blinked the LED
    previousMillis = currentMillis;
    Firebase.setInt(fbdo, path + "/data/value", Detecting_of_dust());
    // Serial.println(Detecting_of_dust());
  }
}

int Detecting_of_dust()
{
  int dustVal = 0;
  int sum = 0;

  for (int i = 0; i < 100; i++)
  {
    /* code */
    // ledPower is any digital pin on the arduino connected to Pin 3 on the sensor
    digitalWrite(ledPower, LOW); // power on the LED
    delayMicroseconds(delayTime);
    dustVal = analogRead(dustPin); // read the dust value via pin 5 on the sensor
    delayMicroseconds(delayTime2);
    digitalWrite(ledPower, HIGH); // turn the LED off
    delayMicroseconds(offTime);
    sum = sum + dustVal;

    if (i == 99)
    {
      /* code */
      sum /= i;
      return sum;
    }
  }
}