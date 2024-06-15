from flask import Flask, request, jsonify
from flask_cors import CORS
import razorpay
import hashlib
import hmac
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
    webhook_secret = Config.RAZORPAY_WEBHOOK_SECRET
    request_data = request.get_data(as_text=True)
    signature = request.headers.get('X-Razorpay-Signature')

    try:
        # Verify the webhook signature
        generated_signature = hmac.new(
            webhook_secret.encode('utf-8'),
            request_data.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()

        if generated_signature != signature:
            return jsonify({'error': 'Invalid signature'}), 400

        # Process the event
        event = request.json
        event_type = event['event']

        if event_type == 'payment.captured':
            payment_id = event['payload']['payment']['entity']['id']
            amount = event['payload']['payment']['entity']['amount']
            # Update your database with the payment information
            # Example: mark the order as paid

        elif event_type == 'payment.failed':
            payment_id = event['payload']['payment']['entity']['id']
            # Update your database with the failure information
            # Example: mark the order as failed

        # Handle other event types as necessary

        return jsonify({'message': 'Webhook processed'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
