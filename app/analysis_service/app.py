from flask import Flask, jsonify, request
from flasgger import Swagger


from controllers.future_dashboard_controller import FutureDashboardController
from controllers.heatmap_controller import HeatMapController
from controllers.option_chain_controller import OptionChainController
from controllers.option_dashboard_controller import OptionDashboardController
from controllers.implied_volatility_controller import ImpliedVolatilityController
from controllers.pcr_controller import PcrController
from controllers.last_quote_controller import LastQuoteController

app = Flask(__name__)

# Swagger configuration
swagger = Swagger(app)

# Routes for fetching stock data
@app.route('/get_ltp', methods=['GET'])
def get_ltp():
    """
    Get the last trade price of a stock by instrument identifier.
    ---
    tags:
      - Stock
    parameters:
      - name: instrument_identifier
        in: query
        type: string
        required: true
        description: Instrument identifier of the stock
    responses:
      200:
        description: Successful operation
      404:
        description: Instrument not found
    """
    instrument_identifier = request.args.get('instrument_identifier')
    ltp = LastQuoteController.get_ltp(instrument_identifier)
    if ltp is not None:
        return jsonify({'InstrumentIdentifier': instrument_identifier, 'LastTradePrice': ltp})
    else:
        return jsonify({'error': 'Instrument not found'}), 404

@app.route('/get_all_instrument_identifiers', methods=['GET'])
def get_all_instrument_identifiers():
    """
    Get all instrument identifiers of available stocks.
    ---
    tags:
      - Stock
    responses:
      200:
        description: Successful operation
    """
    return LastQuoteController.get_all_instrument_identifiers()

@app.route('/get_quote_details', methods=['GET'])
def get_quote_details():
    """
    Get the details of a stock by instrument identifier.
    ---
    tags:
      - Stock
    parameters:
      - name: instrument_identifier
        in: query
        type: string
        required: true
        description: Instrument identifier of the stock
    responses:
      200:
        description: Successful operation
      404:
        description: Instrument details not found
    """
    instrument_identifier = request.args.get('instrument_identifier')
    return LastQuoteController.get_quote_details(instrument_identifier)


# Routes for Option Dashboard
@app.route('/option_dashboard', methods=['GET'])
def get_option_dashboard():
    """
    Get option dashboard data.
    ---
    tags:
      - Stock
    responses:
      200:
        description: Successful operation
    """
    return OptionDashboardController.get_option_dashboard_data()

# Routes for Option Chain
@app.route('/live_option_chain', methods=['GET'])
def get_live_option_chain():
    """
    Get live option chain data.
    ---
    tags:
      - Stock
    responses:
      200:
        description: Successful operation
    """
    return OptionChainController.get_option_chain()

# Routes for pcr_controller
@app.route('/pcr', methods=['GET'])
def get_pcr():
    """
    Get all PCR values of available stocks.
    ---
    tags:
      - Put call Ratio
    responses:
      200:
        description: Successful operation
    """
    return PcrController.get_pcr_data()


# Routes for Implied Volatility
@app.route('/iv_chart', methods=['GET'])
def get_implied_volatility_chart():
    """
    Get IV Chart Data.
    ---
    tags:
      - IV Chart
    responses:
      200:
        description: Successful operation
    """
    return ImpliedVolatilityController.get_iv_chart()


# Routes for Future Dashboard
@app.route('/future_dashboard', methods=['GET'])
def get_future_dashboard():
    """
    Get future dashboard data.
    ---
    tags:
      - Stock
    responses:
      200:
        description: Successful operation
    """
    return FutureDashboardController.get_future_dashboard_data()


# Routes for Heat Map
@app.route('/heat_map', methods=['GET'])
def get_heat_map():
    """
    Get Heat Map Data.
    ---
    tags:
      - Heat Map
    responses:
      200:
        description: Successful operation
    """
    return HeatMapController.get_heat_map()


# Generate Swagger JSON
@app.route('/api/swagger.json')
def generate_swagger():
    return jsonify(swagger.template)

if __name__ == '__main__':
    app.run(debug=True)