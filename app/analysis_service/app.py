from flask import Flask, jsonify, request
from flasgger import Swagger
from flask_socketio import SocketIO


from controllers.future_dashboard_controller import FutureDashboardController
from controllers.heatmap_controller import HeatMapController
from controllers.option_chain_controller import OptionChainController
from controllers.option_dashboard_controller import OptionDashboardController
from controllers.implied_volatility_controller import ImpliedVolatilityController
from controllers.pcr_controller import PcrController


app = Flask(__name__)
socketio = SocketIO(app)

# Swagger configuration
swagger = Swagger(app)


# Routes for Option Dashboard
@app.route('/option_dashboard', methods=['GET'])
def get_option_dashboard():
    return OptionDashboardController.get_option_dashboard_data()

# Routes for Option Chain
@app.route('/live_option_chain', methods=['GET'])
def get_live_option_chain():
    return OptionChainController.get_option_chain()

# Routes for pcr_controller
@app.route('/pcr', methods=['GET'])
def get_pcr():
    return PcrController.get_pcr_data()


# Routes for Implied Volatility
@app.route('/iv_chart', methods=['GET'])
def get_implied_volatility_chart():
    return ImpliedVolatilityController.get_iv_chart()


# Routes for Future Dashboard
@app.route('/future_dashboard', methods=['GET'])
def get_future_dashboard():
    return FutureDashboardController.get_future_dashboard()


# Routes for Heat Map
@app.route('/heat_map', methods=['GET'])
def get_heat_map():
    return HeatMapController.get_heat_map()