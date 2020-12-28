#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

// Set these to run example.
#define FIREBASE_HOST "iot-begin-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "RYAjDY3D1laUkUhk5HmMqVUSy3g61GNOor4wUuL4"
#define WIFI_SSID "win"
#define WIFI_PASSWORD "125478963"

int i = 0;
void setup()
{

    Serial.begin(115200);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("connecting");

    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(500);
    }

    Serial.println();
    Serial.print("connected: ");
    Serial.println(WiFi.localIP());

    Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
}

void loop()
{

    Firebase.setInt("IntNumber", i = random(1, 100));
    if (Firebase.failed())
    {

        Serial.println("set /IntNumber failed:");
        Serial.println(Firebase.error());
        return;
    }

    Serial.print("set /IntNumber to ");
    Serial.println(Firebase.getInt("IntNumber"));

    i++;

    delay(500);
}
