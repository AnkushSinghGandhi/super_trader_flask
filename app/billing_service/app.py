from flask import Flask, request, jsonify
from flask_cors import CORS
import razorpay
from config import Config

app = Flask(__name__)
CORS(app)

razorpay_client = razorpay.Client(auth=(Config.RAZORPAY_API_KEY_ID, Config.RAZORPAY_API_KEY_SECRET))

@app.route('/billing/charge', methods=['POST'])
def charge():
    amount = request.json['amount']  # Amount to be charged
    currency = 'INR'  # Currency (INR for Indian Rupees)
    receipt = 'receipt'  # Unique receipt identifier

    # Create Razorpay order
    try:
        order_response = razorpay_client.order.create({'amount': amount, 'currency': currency, 'receipt': receipt})
        order_id = order_response['id']  # Get order ID from the response

        # Return the order ID to the client
        return jsonify({'order_id': order_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/billing/webhook', methods=['POST'])
def webhook():
    # Handle Razorpay webhook events here
    # Verify the webhook signature and process the event
    # Update payment status in your system accordingly
    return jsonify({'message': 'Webhook received'}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
