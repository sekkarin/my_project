#include <Arduino.h>

#include <ESP8266WiFi.h>

#define SPEED 800
const char *ssid = "win";
const char *password = "125478963";

// Create an instance of the server
// specify the port to listen on as an argument

int moter_A = D3;
int moter_B = D4;
int moter_A_speed = D1;
int moter_B_speed = D2;
int pin_standby = D5;

void up();
void down();
void left();
void right();
void stop_car();

String getHtmlPage();
String css();
String js();
WiFiServer ESPserver(80); // port server

void setup()
{
  Serial.begin(115200);
  // set controlcar
  pinMode(moter_A, OUTPUT);
  pinMode(moter_A_speed, OUTPUT);
  pinMode(moter_B, OUTPUT);
  pinMode(moter_B_speed, OUTPUT);
  pinMode(pin_standby, OUTPUT);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  // wait connected
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(SPEED);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  WiFi.begin(ssid, password);
  // Start the server
  ESPserver.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.println(WiFi.localIP());
}

void loop()
{

  // Check if a client has connected
  WiFiClient client = ESPserver.available();
  if (!client)
  {
    return;
  }

  // Wait until the client sends some data
  Serial.println("new client");
  unsigned long timeout = millis() + 3000;
  while (!client.available() && millis() < timeout)
  {
    delay(1);
  }
  if (millis() > timeout)
  {
    Serial.println("timeout");
    client.flush();
    client.stop();
    return;
  }

  // Read the first line of the request
  String req = client.readStringUntil('\r');
  client.flush();

  Serial.println(req);
  Serial.printf("MOVE");
  if (req.indexOf("/f") != -1)
  {
    up();
    Serial.printf("up");
  }
  else if (req.indexOf("/r") != -1)
  {
    Serial.printf("right");
    right();
  }
  else if (req.indexOf("/l") != -1)
  {
    left();
    Serial.printf("left");
  }
  else if (req.indexOf("/b") != -1)
  {
    down();
    Serial.printf("down");
  }
  else if (req.indexOf("/s") != -1)
  {
    stop_car();
    Serial.printf("break");
  }
  else if (req.indexOf("/c"))
  {
    digitalWrite(pin_standby, HIGH);
  }
  else
  {
    stop_car();
  }

  client.print(getHtmlPage());
  client.flush();
  digitalWrite(pin_standby, LOW);
}
void up()
{
  digitalWrite(moter_A, HIGH);
  analogWrite(moter_A_speed, SPEED);

  digitalWrite(moter_B, LOW);
  analogWrite(moter_B_speed, SPEED);
}
void down()
{
  digitalWrite(moter_A, LOW);
  analogWrite(moter_A_speed, SPEED);

  digitalWrite(moter_B, HIGH);
  analogWrite(moter_B_speed, SPEED);
}

void left()
{

  digitalWrite(moter_A, LOW);
  analogWrite(moter_A_speed, SPEED);

  digitalWrite(moter_B, LOW);
  analogWrite(moter_B_speed, SPEED);
}
void right()
{

  digitalWrite(moter_A, HIGH);
  analogWrite(moter_A_speed, SPEED);

  digitalWrite(moter_B, HIGH);
  analogWrite(moter_B_speed, SPEED);
}
void stop_car()
{
  analogWrite(moter_A_speed, 0);
  analogWrite(moter_B_speed, 0);
}
String getHtmlPage()
{
  String strhtml = "<!DOCTYPE html>";
  strhtml += "<html>";
  strhtml += "<head>";
  strhtml += css();
  strhtml += "<meta charset=\"UTF-8\" http-equiv=\"Content-Type\" content=\"text/html\">";
  strhtml += " <meta name=\"viewport\" content=\"width=device-width, initial-scale=1,height = device-height\">";
  strhtml += " <title>Control_car</title>";
  strhtml += "</head><body onload='init()'>";
  strhtml += "<center><h1>Car control</h1><br>";
  strhtml += "<h3>ปุ่มเตรียมพร้อมการตรวจ</h3><input type=\"button\" value=\"Standby\" id=\"btn_stb\" class=\"button\"><br><hr style=\"width: 25%;\">";
  strhtml += " <input type=\"button\" class=\"button\" id=\"btnf\" value=\"forward\"><br><br>";
  strhtml += " <input type=\"button\" class=\"button\" id=\"btnl\" value=\"<< Left &nbsp;\">";
  strhtml += " <input type=\"button\" class=\"button\" id=\"btnr\" value=\"Right >>\">";
  strhtml += "<br><br>";
  strhtml += "<input type=\"button\" class=\"button\" id=\"btnb\" value=\"backward\">";
  strhtml += "<div id=\"status\">...</div></center></body>";
  strhtml += js();
  strhtml += "</html>";
  return strhtml;
}
String css()
{
  String strcss = "<style>";
  strcss += ".button{background-color: #990033;";
  strcss += "border: none; border-radius: 4px;color: white; padding: 30px 30px; font-size: 20px;";
  strcss += "text-align: center;direction: none;text-decoration: none;}";
  strcss += " </style>";
  return strcss;
}
String js()
{
  String strjs = "<script type=\"text/javascript\">";
  strjs += "function init() { document.getElementById('btnf').addEventListener('touchstart', movef, false);";
  strjs += "document.getElementById('btn_stb').addEventListener('touchstart', Standby_, false);";
  strjs += "document.getElementById('btn_stb').addEventListener('touchend', stopcar, false);";
  strjs += "document.getElementById('btnf').addEventListener('touchend', stopcar, false);";
  strjs += "document.getElementById('btnl').addEventListener('touchstart', movel, false);";
  strjs += "document.getElementById('btnl').addEventListener('touchend', stopcar, false);";
  strjs += "document.getElementById('btnr').addEventListener('touchstart', mover, false);";
  strjs += "document.getElementById('btnr').addEventListener('touchend', stopcar, false);";
  strjs += "document.getElementById('btnb').addEventListener('touchstart', moveb, false);";
  strjs += "document.getElementById('btnb').addEventListener('touchend', stopcar, false);}";
  strjs += "function move(dir){document.getElementById('status').innerHTML = dir;";
  strjs += "var requst = new XMLHttpRequest();";
  strjs += "requst.open('GER', '/engines/'+dir,true);";
  strjs += "requst.send(null);}";
  strjs += "function movef(){move('f');}";
  strjs += "function movel(){move('l');}";
  strjs += " function mover(){move('r');}";
  strjs += "function Standby_() { move('c'); }";
  strjs += "function moveb(){move('b');}";
  strjs += " function stopcar(){document.getElementById('status').innerHTML = 's';";
  strjs += " var requst = new XMLHttpRequest();";
  strjs += "requst.open('GER', '/engines/s',true);";
  strjs += " requst.send(null);}</script>";
  return strjs;
}
