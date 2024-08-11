# backend/app.py

from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='../frontend', static_url_path='')

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
