from flask import jsonify
from app.models.quote_model import QuoteModel

class QuoteController:
    @staticmethod
    def get_ltp(instrument_identifier):
        last_trade_price = QuoteModel.get_last_trade_price(instrument_identifier)
        return jsonify({'InstrumentIdentifier': instrument_identifier, 'LastTradePrice': last_trade_price}) if last_trade_price else jsonify({'error': 'Instrument not found'}), 404

    @staticmethod
    def get_all_instrument_identifiers():
        identifiers = QuoteModel.get_all_instrument_identifiers()
        return jsonify({'instrument_identifiers': identifiers})

    @staticmethod
    def get_quote_details(instrument_identifier):
        quote_details = QuoteModel.get_quote_details(instrument_identifier)
        return jsonify(quote_details) if quote_details else jsonify({'error': 'Instrument details not found'}), 404