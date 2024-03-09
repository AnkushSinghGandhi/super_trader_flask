from flask import jsonify, request
from app.models.user_model import UserModel
from app.models.quote_model import QuoteModel
from datetime import datetime
import bcrypt

class UserController:
    @staticmethod
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = UserModel.get_user_by_username(username)
        if user:
            hashed_password = user.get('password')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                # Check role
                role = user.get('role')
                if role == 'admin':
                    return jsonify({'message': 'Admin login successful'})
                else:
                    # Check account status
                    status = user.get('status')
                    if status == 'active':
                        return jsonify({'message': 'User login successful'})
                    elif status == 'paused':
                        return jsonify({'error': 'Your account is paused. Please contact support.'}), 401
                    elif status == 'banned':
                        return jsonify({'error': 'Your account has been banned.'}), 401
            else:
                return jsonify({'error': 'Invalid username or password'}), 401
        else:
            return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        existing_user = UserModel.get_user_by_username(username)
        if existing_user:
            return jsonify({'error': 'User already exists'}), 409

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        user = {'username': username, 'password': hashed_password}

        UserModel.create_user(user)
        return jsonify({'message': 'Registration successful'})

    @staticmethod
    def buy():
        data = request.get_json()
        instrument_identifier = data.get('instrument_identifier')
        quantity = data.get('quantity')
        user_id = data.get('user_id')

        # Fetch the last trade price for the instrument identifier
        ltp = QuoteModel.get_last_trade_price(instrument_identifier)
        if ltp is None:
            return jsonify({'error': 'Instrument not found'}), 404

        # Calculate the total price
        total_price = ltp * quantity

        # Get the user details
        user = UserModel.get_user_by_id(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        # Store the purchase details in the database
        purchase_data = {
            'datetime': datetime.now(),
            'user_id': user_id,
            'username': user['username'],
            'instrument_identifier': instrument_identifier,
            'quantity': quantity,
            'ltp_at_purchase': ltp,
            'total_price': total_price
        }

        # Save purchase data in the user's purchase history
        UserModel.add_purchase_to_history(user_id, purchase_data)

        return jsonify({'message': 'Purchase successful', 'purchase_data': purchase_data})

    @staticmethod
    def sell():
        data = request.get_json()
        instrument_identifier = data.get('instrument_identifier')
        quantity = data.get('quantity')
        user_id = data.get('user_id')

        # Fetch the last trade price for the instrument identifier
        ltp = QuoteModel.get_last_trade_price(instrument_identifier)
        if ltp is None:
            return jsonify({'error': 'Instrument not found'}), 404

        # Calculate the total price
        total_price = ltp * quantity

        # Get the user details
        user = UserModel.get_user_by_id(user_id)
        if user is None:
            return jsonify({'error': 'User not found'}), 404

        # Retrieve the purchase details from the database
        # This could be your MongoDB query to fetch the purchase data
        # For demonstration purposes, let's assume a dummy purchase data
        purchase_data = {
            'datetime': datetime.now(),
            'user_id': user_id,
            'username': user['username'],
            'instrument_identifier': instrument_identifier,
            'quantity': quantity,
            'ltp_at_purchase': 100,  # Dummy value for demonstration
            'total_price': total_price
        }

        # Calculate the profit or loss
        buying_price = purchase_data['ltp_at_purchase'] * quantity
        selling_price = total_price
        profit_loss = selling_price - buying_price

        # Store the sale details along with profit/loss in the database
        sale_data = {
            'datetime': datetime.now(),
            'user_id': user_id,
            'username': user['username'],
            'instrument_identifier': instrument_identifier,
            'quantity': quantity,
            'ltp_at_sale': ltp,
            'total_price': total_price,
            'profit_loss': profit_loss
        }

        # Save sale data in the user's purchase history
        UserModel.add_sale_to_history(user_id, sale_data)

        return jsonify({'message': 'Sale successful', 'sale_data': sale_data})

    @staticmethod
    def get_purchase_history(user_id):
        user = UserModel.get_user_by_id(user_id)
        if user:
            purchase_history = user.get('purchase_history', [])
            return jsonify({'purchase_history': purchase_history})
        else:
            return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def get_sell_history(user_id):
        user = UserModel.get_user_by_id(user_id)
        if user:
            sell_history = user.get('sell_history', [])
            return jsonify({'sell_history': sell_history})
        else:
            return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def add_watchlist_items(user_id):
        data = request.get_json()
        watchlist = data.get('watchlist', [])
        user = UserModel.get_user_by_id(user_id)
        if user:
            UserModel.update_user(user_id, {'watchlist': watchlist})
            return jsonify({'message': 'watchlist updated successfully'})
        else:
            return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def get_watchlist_items(user_id):
        user = UserModel.get_user_by_id(user_id)
        if user:
            watchlist = user.get('watchlist', [])
            return jsonify({'watchlist': watchlist})
        else:
            return jsonify({'error': 'User not found'}), 404

    @staticmethod
    def delete_watchlist_items(user_id):
        data = request.get_json()
        stock_to_delete = data.get('watchlist', '') # Assuming you provide the stock symbol to delete

        # Fetch the user data
        user = UserModel.get_user_by_id(user_id)
        if user:
            # Check if the stock exists in the user's watchlist
            if stock_to_delete in user.get('watchlist', []):
                # Remove the stock from the watchlist
                watchlist = [stock for stock in user.get('watchlist') if stock != stock_to_delete]
                # Update the user's watchlist
                UserModel.update_user(user_id, {'watchlist': watchlist})
                return jsonify({'message': f'Stock {stock_to_delete} removed from watchlist'})
            else:
                return jsonify({'error': f'Stock {stock_to_delete} not found in watchlist'}), 404
        else:
            return jsonify({'error': 'User not found'}), 404