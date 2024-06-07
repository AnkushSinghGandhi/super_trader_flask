from config import db

last_quote_array = db['last_quote_array']

class LastQuoteArrayModel:
    @staticmethod
    def get_last_quote_array():
        return last_quote_array.find()

    @staticmethod
    def get_last_trade_price(instrument_identifier):
        document = last_quote_array.find_one({'InstrumentIdentifier': instrument_identifier}, sort=[('_id', -1)])

        return document['LastTradePrice'] if document else None

    @staticmethod
    def get_all_instrument_identifiers():
        cursor = last_quote_array.find({}, {'InstrumentIdentifier': 1, '_id': 0})
        return [doc['InstrumentIdentifier'] for doc in cursor]

    @staticmethod
    def get_quote_details(instrument_identifier):
        document = last_quote_array.find_one({'InstrumentIdentifier': instrument_identifier})
        if document:
            # Convert ObjectId to string
            document['_id'] = str(document['_id'])
            return document
        else:
            return None


