from flask import Flask, jsonify
from flasgger import Swagger

from controllers.user_controller import UserController
from controllers.admin_controller import AdminController



app = Flask(__name__)

# Swagger configuration
swagger = Swagger(app)



# Routes for user APIs
@app.route('/login', methods=['POST'])
def login():
    """
    Authenticate a user.
    ---
    tags:
      - Authentication
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Username of the user
      - name: password
        in: formData
        type: string
        required: true
        description: Password of the user
    responses:
      200:
        description: User login successful
      401:
        description: Invalid username or password
      404:
        description: User not found
    """
    return UserController.login()

@app.route('/register', methods=['POST'])
def register():
    """
    Register a new user.
    ---
    tags:
      - Authentication
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Username of the user
      - name: password
        in: formData
        type: string
        required: true
        description: Password of the user
      - name: email
        in: formData
        type: string
        required: true
        description: Email of the user
    responses:
      200:
        description: Registration successful
      409:
        description: User already exists
    """
    return UserController.register()

@app.route('/buy', methods=['POST'])
def buy():
    """
    Buy stocks.
    ---
    tags:
      - Trading
    parameters:
      - name: instrument_identifier
        in: formData
        type: string
        required: true
        description: Instrument identifier of the stock
      - name: Last_Trade_Price
        in: formData
        type: string
        required: true
        description: Last Trade Price of the stock
      - name: quantity
        in: formData
        type: integer
        required: true
        description: Quantity of stocks to buy
      - name: user_id
        in: formData
        type: string
        required: true
        description: ID of the user making the purchase
    responses:
      200:
        description: Purchase successful
      404:
        description: Instrument not found or User not found
    """
    return UserController.buy()

@app.route('/sell', methods=['POST'])
def sell():
    """
    Sell stocks.
    ---
    tags:
      - Trading
    parameters:
      - name: instrument_identifier
        in: formData
        type: string
        required: true
        description: Instrument identifier of the stock
      - name: Last_Trade_Price
        in: formData
        type: string
        required: true
        description: Last Trade Price of the stock
      - name: quantity
        in: formData
        type: integer
        required: true
        description: Quantity of stocks to sell
      - name: user_id
        in: formData
        type: string
        required: true
        description: ID of the user making the sale
    responses:
      200:
        description: Sale successful
      404:
        description: Instrument not found or User not found
    """
    return UserController.sell()

@app.route('/users/<user_id>/purchase_history', methods=['GET'])
def get_purchase_history(user_id):
    """
    Get purchase history of a user.
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    return UserController.get_purchase_history(user_id)

@app.route('/users/<user_id>/sell_history', methods=['GET'])
def get_sell_history(user_id):
    """
    Get sale history of a user.
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    return UserController.get_sell_history(user_id)

@app.route('/users/<user_id>/watchlist', methods=['POST'])
def add_watchlist_items(user_id):
    """
    Add watchlist items for a user.
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
      - name: watchlist
        in: formData
        type: array
        items:
          type: string
        required: true
        description: List of favorite stocks to add
    responses:
      200:
        description: Favorite stocks updated successfully
      404:
        description: User not found
    """
    return UserController.add_watchlist_items(user_id)

@app.route('/users/<user_id>/watchlist', methods=['GET'])
def get_watchlist_items(user_id):
    """
    Get watchlist of a user.
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    return UserController.get_watchlist_items(user_id)

@app.route('/users/<user_id>/delete_watchlist_items', methods=['POST'])
def delete_watchlist_items(user_id):
    """
    Delete favorite symbols of a user.
    ---
    tags:
      - User
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
      - name: watchlist
        in: formData
        type: string
        required: true
        description: Symbol of the favorite stock to delete
    responses:
      200:
        description: Stock removed from favorites
      404:
        description: User not found or Stock not found in favorites
    """
    return UserController.delete_watchlist_items(user_id)

# Routes for admin APIs
@app.route('/create_admin', methods=['POST'])
def create_admin():
    """
    Create an admin account.
    ---
    tags:
      - Admin
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Username of the admin
      - name: password
        in: formData
        type: string
        required: true
        description: Password of the admin
      - name: email
        in: formData
        type: string
        required: true
        description: Email of the admin
    responses:
      200:
        description: Admin created successfully
    """
    return AdminController.create_admin()

@app.route('/create_user', methods=['POST'])
def create_user():
    """
    Create a user account.
    ---
    tags:
      - Admin
    parameters:
      - name: username
        in: formData
        type: string
        required: true
        description: Username of the user
      - name: password
        in: formData
        type: string
        required: true
        description: Password of the user
      - name: email
        in: formData
        type: string
        required: true
        description: Email of the user
      - name: role
        in: formData
        type: string
        required: false
        description: Role of the user (default is 'user')
    responses:
      200:
        description: User created successfully
    """
    return AdminController.create_user()

@app.route('/pause_user', methods=['POST'])
def pause_user():
    """
    Pause a user account.
    ---
    tags:
      - Admin
    parameters:
      - name: user_id
        in: formData
        type: string
        required: true
        description: ID of the user to pause
    responses:
      200:
        description: User paused successfully
    """
    return AdminController.pause_user()

@app.route('/ban_user', methods=['POST'])
def ban_user():
    """
    Ban a user account.
    ---
    tags:
      - Admin
    parameters:
      - name: user_id
        in: formData
        type: string
        required: true
        description: ID of the user to ban
    responses:
      200:
        description: User banned successfully
    """
    return AdminController.ban_user()

@app.route('/get_user_history/<user_id>', methods=['GET'])
def get_user_history(user_id):
    """
    Get purchase history of a user.
    ---
    tags:
      - Admin
    parameters:
      - name: user_id
        in: path
        type: string
        required: true
        description: ID of the user
    responses:
      200:
        description: Successful operation
      404:
        description: User not found
    """
    return AdminController.get_user_history(user_id)

# Generate Swagger JSON
@app.route('/api/swagger.json')
def generate_swagger():
    return jsonify(swagger.template)

if __name__ == '__main__':
    app.run(debug=True)
