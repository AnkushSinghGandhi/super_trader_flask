from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/log', methods=['POST'])
def log():
    data = request.json
    message = data.get('message')
    
    # Log the message
    logging.info(message)

    return jsonify({'message': 'Log recorded successfully'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
