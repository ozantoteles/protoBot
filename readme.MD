# Project README

## Overview

This project is a web application built with Flask that allows users to generate and upload Arduino code for an ESP32C3 microcontroller. The application uses OpenAI's GPT-3.5-turbo model to generate the code based on user input and the Arduino CLI to compile and upload the code to the microcontroller.

## Features

- Generate Arduino code for ESP32C3 based on user instructions.
- List available serial ports.
- Upload generated code to the ESP32C3 microcontroller.

## Prerequisites

- Python 3.7+
- Flask
- OpenAI Python client
- Arduino CLI
- dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:
        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

5. Install Arduino CLI:
    - Follow the instructions on the [Arduino CLI website](https://arduino.github.io/arduino-cli/installation/).

6. Install the necessary Arduino board package:
    ```sh
    arduino-cli core update-index
    arduino-cli core install deneyap:esp32
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Use the web interface to:
    - Generate Arduino code by providing instructions.
    - List available serial ports.
    - Upload the generated code to the ESP32C3 microcontroller.

## File Structure

- `app.py`: Main Flask application file.
- `openai_test.py`: Example script for testing OpenAI API.
- `generated_code.ino`: File where the generated Arduino code is saved.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `templates/index.html`: HTML template for the web interface.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://www.openai.com/)
- [Arduino CLI](https://arduino.github.io/arduino-cli/)

## Contact

For any questions or issues, please open an issue on the GitHub repository.# Project README

## Overview

This project is a web application built with Flask that allows users to generate and upload Arduino code for an ESP32C3 microcontroller. The application uses OpenAI's GPT-3.5-turbo model to generate the code based on user input and the Arduino CLI to compile and upload the code to the microcontroller.

## Features

- Generate Arduino code for ESP32C3 based on user instructions.
- List available serial ports.
- Upload generated code to the ESP32C3 microcontroller.

## Prerequisites

- Python 3.7+
- Flask
- OpenAI Python client
- Arduino CLI
- dotenv

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the environment variables:
    - Create a `.env` file in the project root directory.
    - Add your OpenAI API key to the `.env` file:
        ```env
        OPENAI_API_KEY=your_openai_api_key
        ```

5. Install Arduino CLI:
    - Follow the instructions on the [Arduino CLI website](https://arduino.github.io/arduino-cli/installation/).

6. Install the necessary Arduino board package:
    ```sh
    arduino-cli core update-index
    arduino-cli core install deneyap:esp32
    ```

## Usage

1. Run the Flask application:
    ```sh
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Use the web interface to:
    - Generate Arduino code by providing instructions.
    - List available serial ports.
    - Upload the generated code to the ESP32C3 microcontroller.

## File Structure

- `app.py`: Main Flask application file.
- `openai_test.py`: Example script for testing OpenAI API.
- `generated_code.ino`: File where the generated Arduino code is saved.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `templates/index.html`: HTML template for the web interface.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://www.openai.com/)
- [Arduino CLI](https://arduino.github.io/arduino-cli/)

## Contact

For any questions or issues, please open an issue on the GitHub repository.