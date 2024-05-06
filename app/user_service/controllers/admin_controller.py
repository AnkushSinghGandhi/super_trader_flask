from flask import jsonify, request
from models.user_model import UserModel

class AdminController:
    @staticmethod
    def create_admin():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Logic to create a new admin account
        admin_data = {
            'username': username,
            'password': password,
            'email': email,
            'status': 'active',  # Set default status to active
            'role': 'admin'  # Set role as admin
        }
        UserModel.create_user(admin_data)
        return jsonify({'message': 'Admin created successfully'})

    @staticmethod
    def create_user():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        role = data.get('role', 'user')  # Default role is 'user'

        # Logic to create a new user account
        user_data = {
            'username': username,
            'password': password,
            'email': email,
            'role': role
        }
        UserModel.create_user(user_data)
        return jsonify({'message': 'User created successfully'})
    
    @staticmethod
    def pause_user():
        data = request.get_json()
        user_id = data.get('user_id')

        # Logic to pause a user account
        update_data = {'status': 'paused'}
        UserModel.update_user(user_id, update_data)
        return jsonify({'message': 'User paused successfully'})

    @staticmethod
    def ban_user():
        data = request.get_json()
        user_id = data.get('user_id')

        # Logic to ban a user account
        update_data = {'status': 'banned'}
        UserModel.update_user(user_id, update_data)
        return jsonify({'message': 'User banned successfully'})

    @staticmethod
    def get_user_history(user_id):
        # Logic to fetch the purchase history of a user
        user = UserModel.get_user_by_id(user_id)
        if user:
            purchase_history = user.get('purchase_history', [])
            return jsonify({'purchase_history': purchase_history})
        else:
            return jsonify({'error': 'User not found'}), 404