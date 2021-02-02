
#include <Servo.h>

Servo myservo1;
Servo myservo2;
Servo myservo3; 
Servo myservo4;
int vr_1 = A0;
int vr_2 = A1;
int vr_3 = A2;
int vr_4 = A3;

void setup()
{
    Serial.begin(9600);
    myservo1.attach(3);
    myservo2.attach(5);
    myservo3.attach(6);
    myservo4.attach(9);
    //  pinMode(vr_1, INPUT);
    //  pinMode(vr_2, INPUT);
    //  pinMode(vr_3, INPUT);
    //  pinMode(vr_4, INPUT);
}

void loop()
{
    int pos_servo01 = map(analogRead(vr_1), 0, 1024, 0, 180);
    int pos_servo02 = map(analogRead(vr_2), 0, 1024, 0, 180);
    int pos_servo03 = map(analogRead(vr_3), 0, 1024, 0, 180);
    int pos_servo04 = map(analogRead(vr_4), 0, 1024, 0, 180);
    myservo1.write(pos_servo01);
    myservo1.write(pos_servo02);
    myservo1.write(pos_servo03);
    myservo1.write(pos_servo04);
}
