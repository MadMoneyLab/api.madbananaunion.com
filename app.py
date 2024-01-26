from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__, template_folder='templates')

# Ensure the existence of a data.json file
data_file_path = 'data.json'
if not os.path.exists(data_file_path):
    with open(data_file_path, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_data', methods=['POST'])
def record_data():
    try:
        # Get JSON data from the POST request
        data = request.get_json()

        # Load existing data from the file
        with open(data_file_path, 'r') as f:
            existing_data = json.load(f)

        # Append new data to the existing data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(data_file_path, 'w') as f:
            json.dump(existing_data, f)

        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)