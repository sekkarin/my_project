// ArduinoJson - arduinojson.org
// Copyright Benoit Blanchon 2014-2019
// MIT License
//
// This example shows how to generate a JSON document with ArduinoJson.

#include <ArduinoJson.h>
int  num_2;
unsigned int num_1;
unsigned long previousMillis = 100; // will store last time LED was updated
char get_status_led;

// constants won't change:
const long interval = 10; // interval at which to blink (milliseconds)
void add_value(unsigned int num_1, int num_2,int num_3);

void setup()
{

    Serial.begin(115200);
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= interval)
    {
        previousMillis = currentMillis;
        num_1++;
        add_value(num_1, num_2,NULL);
    }

    if (Serial.available() > 0)
    {
        
        get_status_led = Serial.read();
        if (get_status_led == '1')
        {
            digitalWrite(LED_BUILTIN, HIGH);
        }
        else if (get_status_led == '0')
        {
            digitalWrite(LED_BUILTIN, LOW);
        }
        add_value(num_1, num_2,get_status_led);
    }
}

void add_value(unsigned int num_1, int num_2,int num_3)
{
    StaticJsonBuffer<200> jsonBuffer;

    JsonObject &root = jsonBuffer.createObject();

    JsonArray &data = root.createNestedArray("data");

    data.add(num_1);
    data.add(num_2 = random(1, 100));
    data.add(num_3);
    root.printTo(Serial);
    Serial.println();
    //  root.prettyPrintTo(Serial);
}