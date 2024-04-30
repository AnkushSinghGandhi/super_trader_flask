from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from config import *

app = Flask(__name__)
CORS(app)

# API Gateway routes
@app.route('/user/<path:path>', methods=['GET', 'POST'])
def user(path):
    url = f"{USER_SERVICE_URL}/{path}"
    response = requests.request(request.method, url, json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/billing/<path:path>', methods=['GET', 'POST'])
def billing(path):
    url = f"{BILLING_SERVICE_URL}/{path}"
    response = requests.request(request.method, url, json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/logging/<path:path>', methods=['POST'])
def logging(path):
    url = f"{LOGGING_SERVICE_URL}/{path}"
    response = requests.post(url, json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/analysis/<path:path>', methods=['GET', 'POST'])
def analysis(path):
    url = f"{ANALYSIS_SERVICE_URL}/{path}"
    response = requests.request(request.method, url, json=request.json)
    return jsonify(response.json()), response.status_code

@app.route('/trade/<path:path>', methods=['GET', 'POST'])
def trade(path):
    url = f"{TRADE_SERVICE_URL}/{path}"
    response = requests.request(request.method, url, json=request.json)
    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
