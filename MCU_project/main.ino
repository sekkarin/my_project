#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>

// set name and password
#ifndef APSSID
#define APSSID "Project_1"
#define APPSK ""
#endif

const char *ssid = APSSID;
const char *password = APPSK;

ESP8266WebServer server(80);

float TempCstat;
float Humiditystat;
void handle_OnConnect()
{
    TempCstat = random(0, 100);   // Gets the values of the temperature
    Humiditystat = random(0, 50); // Gets the values of the humidity
    server.send(200, "text/html", SendHTML(TempCstat, Humiditystat)); // Respone Home page
}
void setup()
{
    delay(1000);
    Serial.begin(115200);
    Serial.println();
    Serial.print("Configuring access point...");
    //set ip static
    IPAddress local_ip = {1, 1, 1, 1};
    IPAddress gateway = {192, 168, 1, 1};
    IPAddress subnet = {255, 255, 255, 0};

    WiFi.softAPConfig(local_ip, gateway, subnet);
    //display IP
    IPAddress myIP = WiFi.softAPIP();
    Serial.print("AP IP address: ");
    Serial.println(myIP);
    // home page
    server.on("/", handle_OnConnect);
    server.begin();
    Serial.println("HTTP server started");
}

void loop()
{
    server.handleClient();
}

//index html
String SendHTML(float TempCstat, float Humiditystat)
{

    String ptr = "<!DOCTYPE html> <html>\n";
    ptr += "<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
    // title
    ptr += "<title>ESP8266 Weather Report</title>\n";
    // style
    ptr += "<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}\n";
    ptr += "body{margin-top: 50px;} h1 {color: #444444;margin: 50px auto 30px;}\n";
    ptr += "p {font-size: 24px;color: #444444;margin-bottom: 10px;}\n";
    ptr += "</style>\n";
    //javascritpt
    ptr += js();
    ptr += "</head>\n";
    //Body
    ptr += "<body>\n";
    ptr += "<div id=\"webpage\">\n";
    ptr += "<h1>ESP8266 NodeMCU Weather Report</h1>\n";
    // DISPLAY Value
    ptr += "<p>Temperature: ";
    ptr += (int)TempCstat;
    ptr += "°C</p>";
    ptr += "<p>Humidity: ";
    ptr += (int)Humiditystat;
    ptr += "%</p>";

    ptr += "</div>\n";
    ptr += "</body>\n";
    ptr += "</html>\n";
    return ptr;
}

//javascript and ajex 
String js()
{
    String ptr = "";
    ptr += "<script>\n";
    ptr += "setInterval(loadDoc,1500);\n";
    ptr += "function loadDoc() {\n";
    ptr += "var xhttp = new XMLHttpRequest();\n";
    ptr += "xhttp.onreadystatechange = function() {\n";
    ptr += "if (this.readyState == 4 && this.status == 200) {\n";
    ptr += "document.getElementById(\"webpage\").innerHTML =this.responseText}\n";
    ptr += "};\n";
    ptr += "xhttp.open(\"GET\", \"/\", true);\n";
    ptr += "xhttp.send();\n";
    ptr += "}\n";
    ptr += "</script>\n";
    return ptr;
}