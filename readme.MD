# ProtoBot: AI-Driven Code-Free Prototyping for Wearable Electronics

![ProtoBot Logo](https://github.com/ozantoteles/protoBot/blob/master/images/protobot_logo.jpg)

[![License](https://img.shields.io/github/license/ozantoteles/protobot)](LICENSE)  
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-2.0%2B-blue.svg)](https://flask.palletsprojects.com/)  
[![OpenAI](https://img.shields.io/badge/OpenAI-API-brightgreen.svg)](https://openai.com/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Electronic Components](#electronic-components)
- [Case Study](#case-study)
- [Lessons Learned](#lessons-learned)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgements](#acknowledgements)
- [References](#references)

## Introduction

**ProtoBot** is an AI-driven chatbot designed to empower individuals with limited software and hardware expertise to prototype wearable electronic devices without writing any code. Leveraging large language models (LLMs) and integrating seamlessly with Arduino-compatible hardware, ProtoBot simplifies the prototyping process through intuitive prompt-based interactions.

By transforming uncertainty into a positive and motivating experience, ProtoBot serves as a reliable guide, enabling non-experts to explore and create innovative wearable technology solutions effortlessly.

## Features

- **Code-Free Prototyping:** Generate Arduino code through natural language prompts without needing to write code manually.
- **Interactive Chat Interface:** Engage in continuous, context-aware conversations with ProtoBot to iteratively develop your wearable device.
- **Seamless Hardware Integration:** Compatible with Arduino-based development boards and Deneyap G boards, supporting various sensors and actuators.
- **Real-Time Code Uploading:** Upload generated code directly to your hardware using the Arduino CLI.
- **User-Friendly Interface:** Intuitive web-based interface built with Flask for easy interaction and management.
- **Extensible Design:** Easily add support for additional hardware components and extend ProtoBot’s capabilities.

## Demo

![ProtoBot Interface](https://github.com/ozantoteles/protoBot/blob/master/images/protobot_interface.png)

*Figure 1: ProtoBot User Interface featuring the Chat Interface and Arduino CLI Interaction Panel.*

## Installation

### Prerequisites

- **Python 3.8+**
- **Arduino CLI:** Ensure `arduino-cli` is installed and added to your system's PATH.
- **OpenAI API Key:** Obtain an API key from [OpenAI](https://openai.com/api/).

### Clone the Repository

```bash
git clone https://github.com/ozantoteles/protobot.git
cd protobot
```

### Set Up Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Initialize Arduino CLI

Ensure that the Arduino CLI is properly configured. You may need to set up your board definitions and ensure that your Deneyap G board is recognized.

```bash
arduino-cli config init
arduino-cli core update-index
arduino-cli core install deneyap:esp32
```

## Usage

### Running the Application

Start the Flask application:

```bash
python app.py
```

Open your web browser and navigate to `http://localhost:5000` to access ProtoBot.

### Interacting with ProtoBot

1. **Start a Conversation:** Enter natural language prompts describing the wearable device you wish to create.
2. **Generate Code:** ProtoBot will generate the corresponding Arduino code based on your prompts.
3. **Upload Code:** Use the Arduino CLI Interaction Panel to compile and upload the code to your connected device.
4. **Iterate:** Continue refining your device by providing additional prompts or adjusting parameters as needed.

### Resetting the Chat

To start a new conversation, click the "Reset Chat" button, which clears the current chat history and allows you to begin fresh.

## Electronic Components

ProtoBot is optimized for use with **Deneyap G** boards and the accompanying sensors and actuators from Deneyap's Prototyping Kits, including:

- **Deneyap G Board:** Arduino-compatible microcontroller designed for wearable electronics.
- **Deneyap Card Robotics Programming Set:** Includes sensors and actuators for robotic applications.
- **Deneyap Card Smart Home Set:** Components for creating smart home wearable devices.

### Supported Sensors and Actuators

![Sensors and Actuators](https://github.com/ozantoteles/protoBot/blob/master/images/sa.png)

*Figure 2: Sensors and Actuators Used in the Study.*

- **Sensors:**
  - Line Following Sensor
  - Microphone
  - APDS-9960 (RGB, Ambient Light, Proximity, Gesture)
  - SHTC3 (Temperature and Humidity)
  - LSM6DSM (IMU)
  - MSP430G2352 (Touchpad)
  - PIR Sensor
  - VL53L0CXV0DH/1 (Time of Flight)
  - IR Transmitter and Receiver
  - LTR-553ALS-01 (Ambient Light)

- **Actuators:**
  - Addressable RGB LED
  - Speaker
  - 5x7 LED Matrix
  - OLED Display
  - Relay
  - Battery (3.7V 1800mAh Lithium Polymer)

For detailed information on each component, refer to the [Deneyap Prototyping Kits](https://github.com/deneyapgithub).

## Case Study

We conducted a case study involving four professionals from diverse disciplines to evaluate ProtoBot's effectiveness in enabling code-free wearable prototyping. The participants developed four distinct wearable device concepts:

1. **GuidingSteps:** Footwear that guides each step you take, aiding navigation without the need to check a smartphone.
2. **BakeHero Glove:** Encourages quick action in the kitchen by gamifying the process of removing muffins from the oven.
3. **PedalPulse:** Provides visual feedback on cycling intensity to help cyclists manage their performance and hydration.
4. **FitFit:** Enhances the connection between a user and their cat by providing feedback on the cat's interactions with the litter box.

![Case Study Concepts](https://github.com/ozantoteles/protoBot/blob/master/images/case-ALL.jpg)

*Figure 3: Wearable device concepts generated by participants: GuidingSteps, BakeHero Glove, PedalPulse, and FitFit.*

### Highlights

- **GuidingSteps:** Utilized IMU sensors and LED matrices to provide directional cues.
- **BakeHero Glove:** Employed temperature sensors and LED matrices to indicate when it's safe to remove items from the oven.
- **PedalPulse:** Integrated IMU sensors and RGB LEDs to monitor and display cycling intensity.
- **FitFit:** Combined IMU sensors and RGB LEDs to track and provide feedback on cat movements.

## Lessons Learned

### 1. Turning Uncertainty Into a Positive Experience

Participants initially felt uncertain about working with unfamiliar electronic components. However, ProtoBot transformed this uncertainty into a motivating and exciting exploration process. By facilitating a playful interaction with hardware components, ProtoBot enabled users to overcome anxiety and engage creatively in prototyping.

### 2. ProtoBot Acting as a Reliable Guide

ProtoBot demonstrated significant potential as a reliable guide for users with limited expertise. Participants appreciated how ProtoBot could assist in generating accurate code, although they suggested enhancements like asking for component photos to improve response accuracy. Future iterations aim to make ProtoBot even more dependable by expanding its training and hardware support.

### 3. Adjusting Design Parameters When Interacting With the Prototypes

Users expressed the need to adjust design parameters without re-entering prompts. ProtoBot currently generates code based on user inputs, but providing an interface for parameter tuning would allow for more flexible and iterative refinement of prototypes. This feature is crucial for real-world applications where fine-tuning is often required.

## Contributing

We welcome contributions to enhance ProtoBot! Whether you're reporting issues, suggesting features, or submitting pull requests, your input is invaluable.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

Please adhere to our [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Authors

- **Ihsan Ozan Yıldırım** - [@ihsanozan](https://github.com/ozantoteles)
- **Cansu Çetin Er** - [@cansucetin](https://github.com/cans91)
- **Ege Keskin** - [@egekeskin](https://github.com/ege621)

See also the list of [contributors](https://github.com/ozantoteles/protobot/contributors) who participated in this project.

## Acknowledgements

- Special thanks to the participants of our case study for their valuable feedback and innovative ideas.
- Gratitude to [OpenAI](https://openai.com/) for providing the ChatGPT API.
- Appreciation for the Deneyap team for their versatile prototyping kits and hardware.

## References

- Yıldırım, I. O., Er, C. Ç., Keskin, E., Kuşcu, M., & Özcan, O. (2024). From Uncertainty to Innovation: Wearable Prototyping with ProtoBot. *ArXiv Preprint*. [arXiv:XXXX.XXXX](https://arxiv.org/abs/XXXX.XXXX)
- Buechley, L. (2008). Lilypad.
- OpenAI API Reference. [OpenAI](https://beta.openai.com/docs/api-reference/)
- Arduino CLI Documentation. [Arduino](https://arduino.github.io/arduino-cli/latest/)
- Deneyap Prototyping Kits. [Deneyap GitHub](https://github.com/deneyapgithub)
- Additional references as cited in the publication.

---

*This README was generated based on the research article "From Uncertainty to Innovation: Wearable Prototyping with ProtoBot" and the ProtoBot Flask application code.*
