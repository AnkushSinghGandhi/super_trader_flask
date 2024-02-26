from app import app
from app.controllers.quote_controller import QuoteController
from app.controllers.user_controller import UserController
from flask import request

# Routes for fetching stock data
@app.route('/get_ltp', methods=['GET'])
def get_ltp():
    instrument_identifier = request.args.get('instrument_identifier')
    return QuoteController.get_ltp(instrument_identifier)

@app.route('/get_all_instrument_identifiers', methods=['GET'])
def get_all_instrument_identifiers():
    return QuoteController.get_all_instrument_identifiers()

# Routes for users
@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@app.route('/register', methods=['POST'])
def register():
    return UserController.register()

@app.route('/buy', methods=['POST'])
def buy():
    return UserController.buy()

@app.route('/sell', methods=['POST'])
def sell():
    return UserController.sell()

@app.route('/user/<user_id>/purchase_history', methods=['GET'])
def get_purchase_history(user_id):
    return UserController.get_purchase_history(user_id)

@app.route('/user/<user_id>/sell_history', methods=['GET'])
def get_sell_history(user_id):
    return UserController.get_sell_history(user_id)


if __name__ == '__main__':
    app.run(debug=True)