from flask import jsonify
from models.last_quote_array import LastQuoteArrayModel

class LastQuoteController:
    @staticmethod
    def get_ltp(instrument_identifier):
        last_trade_price = LastQuoteArrayModel.get_last_trade_price(instrument_identifier)
        return last_trade_price

    @staticmethod
    def get_all_instrument_identifiers():
        identifiers = LastQuoteArrayModel.get_all_instrument_identifiers()
        return jsonify({'instrument_identifiers': identifiers})

    @staticmethod
    def get_quote_details(instrument_identifier):
        quote_details = LastQuoteArrayModel.get_quote_details(instrument_identifier)
        return jsonify(quote_details) if quote_details else jsonify({'error': 'Instrument details not found'}), 404