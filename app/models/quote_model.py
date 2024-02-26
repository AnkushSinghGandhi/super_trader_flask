from app.config import db

last_quote_array = db['last_quote_array']

class QuoteModel:
    @staticmethod
    def get_last_trade_price(instrument_identifier):
        document = last_quote_array.find_one({'InstrumentIdentifier': instrument_identifier})
        return document['LastTradePrice'] if document else None

    @staticmethod
    def get_all_instrument_identifiers():
        cursor = last_quote_array.find({}, {'InstrumentIdentifier': 1, '_id': 0})
        return [doc['InstrumentIdentifier'] for doc in cursor]