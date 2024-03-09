from app.config import db

user_collection = db['users']

class UserModel:

    @staticmethod
    def create_user(username, password, email, role='user'):
        # Logic to create a new user account
        user_data = {
            'username': username,
            'password': password,
            'email': email,
            'role':role, # Set user role
            'status': 'active',  # Set default status to active
            'purchase_history': [],  # Initialize purchase history as empty list
            'sale_history': [],  # Initialize sale history as empty list
            'watchlist': []  # Initialize watchlist as empty list
        }
        user_collection.insert_one(user_data)
        return {'message': 'User created successfully'}

    @staticmethod
    def get_user_by_id(user_id):
        return user_collection.find_one({'_id': user_id})

    @staticmethod
    def update_user(user_id, update_data):
        user_collection.update_one({'_id': user_id}, {'$set': update_data})
        return {'message': 'User updated successfully'}

    @staticmethod
    def get_user_by_username(username):
        return user_collection.find_one({'username': username})

    @staticmethod
    def add_purchase_to_history(user_id, purchase_data):
        user_collection.update_one({'_id': user_id}, {'$push': {'purchase_history': purchase_data}})

    @staticmethod
    def add_sale_to_history(user_id, sale_data):
        user_collection.update_one({'_id': user_id}, {'$push': {'sale_history': sale_data}})