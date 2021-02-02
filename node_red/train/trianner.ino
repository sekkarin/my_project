
#include <Arduino_JSON.h>
unsigned long get_milis = 0;
const long delay_time = 2000;
String get_stingjson;
void setup()
{
  Serial.begin(115200);
  while (!Serial)
    ;
  objectDemo();
}

void loop()
{
  unsigned long cout_milis = millis();
  if (cout_milis - get_milis >= delay_time)
  {
    get_milis = cout_milis;
    objectDemo();
  }
  if (Serial.available() > 0)
  {  
   get_stingjson = Serial.readString(); // read the incoming byte:
  }
}
void objectDemo()
{
  JSONVar odd;
  int num1 = 5;
  int num2 = 10;
  odd["data"]["num1"] = num1 = random(0, 100);
  odd["data"]["num2"] = num2 = random(1, 1000);
  odd["data"]["msg_statsu"] = get_stingjson;

  Serial.println(odd);
}
