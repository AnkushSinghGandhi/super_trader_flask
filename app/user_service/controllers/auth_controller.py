from flask import request, jsonify
from models.user_model import User
from app import bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user_model import UserModel
from app.user_service.auth import encode_auth_token


class AuthController:
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
                    auth_token = encode_auth_token(user.id)
                    return jsonify({'auth_token': auth_token}), 200
                else:
                    # Check account status
                    status = user.get('status')
                    if status == 'active':
                        auth_token = encode_auth_token(user.id)
                        return jsonify({'auth_token': auth_token}), 200
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
        # Generate and return JWT token upon successful registration
        auth_token = encode_auth_token(user.id)
        return jsonify({'auth_token': auth_token}), 201

    @jwt_required()
    def logout():
        # Since JWT tokens are stateless, there's no explicit logout like in Flask-Login.
        # Clients can discard or blacklist tokens on their end.
        return jsonify({'message': 'Logout successful'}), 200

    @jwt_required()
    def delete_account():
        current_user_id = get_jwt_identity()
        user = User.get_user_by_id(current_user_id)
        user.delete_account()
        return jsonify({'message': 'Account deleted successfully'}), 200

    @jwt_required()
    def send_verification_email():
        data = request.json
        email = data.get('email')

        user = User.get_user_by_email(email)
        if user:
            token = user.generate_verification_token()
            user.save()  # Save the user with updated verification token
            user.send_verification_email()
            return jsonify({'message': 'Verification email sent successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    @jwt_required()
    def verify_email(token):
        current_user_id = get_jwt_identity()
        user = User.get_user_by_id(current_user_id)
        if user:
            if user.verify_email(token):
                return jsonify({'message': 'Email verified successfully'}), 200
            else:
                return jsonify({'error': 'Invalid verification token'}), 400
        else:
            return jsonify({'error': 'User not found'}), 404

    @jwt_required()
    def request_password_reset():
        data = request.json
        email = data.get('email')

        user = User.get_user_by_email(email)
        if user:
            user.request_password_reset()
            return jsonify({'message': 'Password reset email sent successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404

    @jwt_required()
    def reset_password():
        data = request.json
        token = data.get('token')
        new_password = data.get('new_password')

        current_user_id = get_jwt_identity()
        user = User.get_user_by_id(current_user_id)
        if user:
            if user.reset_password(token, new_password):
                return jsonify({'message': 'Password reset successfully'}), 200
            else:
                return jsonify({'error': 'Invalid or expired reset password token'}), 400
        else:
            return jsonify({'error': 'User not found'}), 404
