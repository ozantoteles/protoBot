import os
from flask import Flask, render_template, request, jsonify, session
import serial.tools.list_ports
from dotenv import load_dotenv
import subprocess
from openai import OpenAI
import logging
import re

logging.basicConfig(level=logging.DEBUG)

load_dotenv()

# Full path to arduino-cli executable
ARDUINO_CLI_PATH = 'arduino-cli'  # Update if needed

def extract_code(response_text):
    # Split the response into lines
    lines = response_text.split('\n')

    # Variables to track if we're inside a code block
    inside_code_block = False
    code_lines = []

    # Iterate over each line and filter out non-code content
    for line in lines:
        # Detect code fences and toggle the inside_code_block flag
        if '```' in line:
            inside_code_block = not inside_code_block
            continue  # Skip the code fence line itself

        # If we're inside a code block, collect the code lines
        if inside_code_block:
            code_lines.append(line)

    # Join the valid code lines back together
    return '\n'.join(code_lines)

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for session management

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for generating code with continuous conversation
@app.route('/generate_code', methods=['POST'])
def generate_code():
    user_input = request.json.get('user_input')

    # Initialize chat history in session if not present
    if 'chat_history' not in session:
        session['chat_history'] = []

    # Append the user's message to the chat history
    session['chat_history'].append({"role": "user", "content": user_input})

    # Prepare the chat messages with history
    messages = [{"role": "system", "content": "You are an expert Arduino programmer. Only return valid and complete Arduino code, without any explanations or comments."}]
    messages += session['chat_history']

    try:
        # Send the chat history to OpenAI to generate or update the code
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.5,
        )

        # Get the chatbot's response
        code_response = response.choices[0].message.content.strip()

        # Post-process the response to extract only the code
        extracted_code = extract_code(code_response)

        # Append the chatbot's response to the chat history
        session['chat_history'].append({"role": "assistant", "content": extracted_code})

        return jsonify({'code': extracted_code})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/get_serial_ports', methods=['GET'])
def get_serial_ports():
    try:
        logging.debug("Attempting to fetch serial ports.")
        ports = serial.tools.list_ports.comports()
        port_list = [{'device': port.device, 'description': port.description} for port in ports]
        logging.debug(f"Found ports: {port_list}")
        return jsonify(port_list)
    except Exception as e:
        logging.error(f"Error fetching serial ports: {str(e)}")
        return jsonify({'error': f'Error fetching serial ports: {str(e)}'}), 500

# Route for uploading code (no change needed here)
@app.route('/upload_code', methods=['POST'])
def upload_code():
    code = request.json.get('code')
    port = request.json.get('port')
    if not code or not port:
        return jsonify({'status': 'error', 'message': 'Code or port not provided.'}), 400

    # Define the sketch name
    SKETCH_NAME = 'generated_code'

    # Define the sketch directory path
    sketch_dir = os.path.join(os.getcwd(), SKETCH_NAME)

    # Create the directory if it doesn't exist
    if not os.path.exists(sketch_dir):
        os.makedirs(sketch_dir)

    # Save the code to a file inside the sketch directory
    code_file = os.path.join(sketch_dir, f'{SKETCH_NAME}.ino')
    with open(code_file, 'w') as f:
        f.write(code)

    # Compile and upload the code using Arduino CLI
    FQBN = 'deneyap:esp32:dyg_mpv10'  # Correct FQBN for your Deneyap board
    compile_command = f'arduino-cli compile --fqbn {FQBN} "{sketch_dir}"'
    upload_command = f'arduino-cli upload -p {port} --fqbn {FQBN} "{sketch_dir}"'

    try:
        # Compile the code
        compile_output = subprocess.check_output(compile_command, shell=True, stderr=subprocess.STDOUT)
        # Upload the code
        upload_output = subprocess.check_output(upload_command, shell=True, stderr=subprocess.STDOUT)
        return jsonify({'status': 'success', 'message': 'Code uploaded successfully!'})
    except subprocess.CalledProcessError as e:
        error_message = e.output.decode()
        return jsonify({'status': 'error', 'message': error_message}), 500

# Route to reset the chat history (for starting over)
@app.route('/reset_chat', methods=['POST'])
def reset_chat():
    session.pop('chat_history', None)
    return jsonify({'status': 'success', 'message': 'Chat history cleared.'})

@app.route('/perform_action', methods=['POST'])
def perform_action():
    data = request.json
    code = data.get('code')
    port = data.get('port')
    action = data.get('action')

    # Define the sketch name and path
    SKETCH_NAME = 'generated_code'
    sketch_dir = os.path.join(os.getcwd(), SKETCH_NAME)
    if not os.path.exists(sketch_dir):
        os.makedirs(sketch_dir)

    # Save the code to the sketch file
    code_file = os.path.join(sketch_dir, f'{SKETCH_NAME}.ino')
    with open(code_file, 'w') as f:
        f.write(code)

    FQBN = 'deneyap:esp32:dyg_mpv10'  # Adjust based on your board

    # Initialize message output
    output_message = ""

    try:
        # Compile the code
        if action in ['compile', 'compile_upload']:
            compile_command = f'"{ARDUINO_CLI_PATH}" compile --fqbn {FQBN} "{sketch_dir}"'
            compile_output = subprocess.check_output(compile_command, shell=True, stderr=subprocess.STDOUT).decode()
            output_message += "Compilation Output:\n" + compile_output + "\n"

        # Upload the code
        if action in ['upload', 'compile_upload']:
            upload_command = f'"{ARDUINO_CLI_PATH}" upload -p {port} --fqbn {FQBN} "{sketch_dir}"'
            upload_output = subprocess.check_output(upload_command, shell=True, stderr=subprocess.STDOUT).decode()
            output_message += "Upload Output:\n" + upload_output + "\n"

        return jsonify({'message': output_message})

    except subprocess.CalledProcessError as e:
        error_message = e.output.decode()
        return jsonify({'message': f'Error during {action.replace("_", " ")}.\n{error_message}'}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)