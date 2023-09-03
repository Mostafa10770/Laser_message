#include <Arduino.h>
#include <Wire.h> // If needed for laser communication
#include <SoftwareSerial.h> // If needed for serial communication

const int laserPin = 2; // Replace with the actual pin number connected to the laser sensor
String receivedData = "";

void setup() {
    pinMode(laserPin, INPUT);
    Serial.begin(9600); // Set up the serial communication
    // Additional setup if needed
}

void loop() {
    char receivedBit = digitalRead(laserPin) == HIGH ? '1' : '0';
    if (receivedBit == '0' || receivedBit == '1') {
        receivedData += receivedBit;
    } else {
        if (!receivedData.isEmpty()) {
            processReceivedData(receivedData);
            receivedData = "";
        }
    }
}

void processReceivedData(String data) {
    char receivedChar = binaryStringToChar(data);
    Serial.print("Received character: ");
    Serial.println(receivedChar);
}

char binaryStringToChar(String binaryString) {
    // Convert binary string to character here
    // Return character
}
