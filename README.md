<!DOCTYPE html>
<html>
<head>
    <title>Arduino Laser Communication Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
        }
        h1 {
            color: #333;
        }
        h2 {
            color: #555;
        }
        p {
            color: #777;
        }
        pre {
            background-color: #f5f5f5;
            padding: 10px;
            border: 1px solid #ddd;
        }
    </style>
</head>
<body>
    <h1>Arduino Laser Communication Project</h1>
    <p>This project showcases a communication system using lasers and Arduino boards. One Arduino functions as the sender, converting text to binary and transmitting it using a laser module. The other Arduino serves as the receiver, decoding the received binary data and displaying the original text.</p>

    <h2>Features</h2>
    <ul>
        <li>Communication between sender and receiver using lasers</li>
        <li>Text-to-binary conversion and transmission</li>
        <li>Binary-to-text conversion and reception</li>
        <li>Basic error handling for received data</li>
    </ul>

    <h2>Setup</h2>
    <ol>
        <li>Connect the laser module to the sender Arduino's designated pin.</li>
        <li>Connect the laser sensor to the receiver Arduino's designated pin.</li>
        <li>Upload the corresponding Arduino code to both sender and receiver Arduinos.</li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Power up both sender and receiver Arduinos.</li>
        <li>Control the sender Arduino using a Python script or the Arduino Serial Monitor.</li>
        <li>The receiver Arduino will decode the received data and display it in the Serial Monitor.</li>
    </ol>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to open issues or pull requests for bug fixes or improvements.</p>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
