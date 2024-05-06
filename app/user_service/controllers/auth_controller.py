from flask import request, jsonify
from app.models.user_model import User
from app import bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.get_user_by_email(email)
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user._id))
        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

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
