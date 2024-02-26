class UserModel:
    # In a real application, you would have methods to fetch user details from the database
    @staticmethod
    def get_user_by_id(user_id):
        # Example: Query the database to get user details by user_id
        return {'id': user_id, 'username': f'user{user_id}'}