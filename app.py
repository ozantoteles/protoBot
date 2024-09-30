import os
from flask import Flask, render_template, request, jsonify
import serial.tools.list_ports
from dotenv import load_dotenv
import subprocess
from openai import OpenAI

load_dotenv()

app = Flask(__name__)

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_code', methods=['POST'])
def generate_code():
    user_input = request.json.get('user_input')
    messages = [
        {
            "role": "system",
            "content": "You are an expert Arduino programmer."
        },
        {
            "role": "user",
            "content": f"Generate Arduino code for an ESP32C3 based on the following instructions:\n{user_input}\n\nPlease provide only the code without additional explanations."
        }
    ]
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.5,
        )
        code = response.choices[0].message.content.strip()
        return jsonify({'code': code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_serial_ports', methods=['GET'])
def get_serial_ports():
    ports = serial.tools.list_ports.comports()
    port_list = [{'device': port.device, 'description': port.description} for port in ports]
    return jsonify(port_list)

@app.route('/upload_code', methods=['POST'])
def upload_code():
    code = request.json.get('code')
    port = request.json.get('port')
    if not code or not port:
        return jsonify({'status': 'error', 'message': 'Code or port not provided.'}), 400

    # Save the code to a file
    code_file = 'generated_code.ino'
    with open(code_file, 'w') as f:
        f.write(code)

    # Compile and upload the code using Arduino CLI
    compile_command = f'arduino-cli compile --fqbn deneyap:esp32:deneyapmini {code_file}'
    upload_command = f'arduino-cli upload -p {port} --fqbn deneyap:esp32:deneyapmini {code_file}'
    try:
        # Compile the code
        compile_output = subprocess.check_output(compile_command, shell=True, stderr=subprocess.STDOUT)
        # Upload the code
        upload_output = subprocess.check_output(upload_command, shell=True, stderr=subprocess.STDOUT)
        return jsonify({'status': 'success', 'message': 'Code uploaded successfully!'})
    except subprocess.CalledProcessError as e:
        error_message = e.output.decode()
        return jsonify({'status': 'error', 'message': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
