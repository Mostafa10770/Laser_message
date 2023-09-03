# Arduino Laser Communication Project

![laser Logo](https://www.nasa.gov/sites/default/files/thumbnails/image/image_for_lcrd_feature_one.jpg)

This project showcases a communication system using lasers and Arduino boards. One Arduino functions as the sender, converting text to binary and transmitting it using a laser module. The other Arduino serves as the receiver, decoding the received binary data and displaying the original text.

## Features
- Communication between sender and receiver using lasers.
- Text-to-binary conversion and transmission.
- Binary-to-text conversion and reception.
- Basic error handling for received data.

## Setup
1. Connect the laser module to the sender Arduino's designated pin.
2. Connect the laser sensor to the receiver Arduino's designated pin.
3. Upload the corresponding Arduino code to both sender and receiver Arduinos.

## Usage
1. Power up both sender and receiver Arduinos.
2. Control the sender Arduino using a Python script or the Arduino Serial Monitor.
3. The receiver Arduino will decode the received data and display it in the Serial Monitor.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests for bug fixes or improvements.

## License
This project is licensed under the [MIT License](LICENSE).
