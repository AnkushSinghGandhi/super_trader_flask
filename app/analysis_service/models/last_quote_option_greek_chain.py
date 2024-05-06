from datetime import datetime
from config import db

lastquoteoptiongreekschain = db["last_quote_option_greek_chain"]


class LastQuoteOptionChainModel:
    @staticmethod
    def get_option_greek_chain():
        return lastquoteoptiongreekschain.find()

    @staticmethod
    def extract_date(instrument_identifier):
        # Split the instrument identifier by underscores and get the third part
        date_part = instrument_identifier.split('_')[2]
        # Extract the date dynamically
        return datetime.strptime(date_part, "%d%b%Y").strftime("%d-%m-%Y")

    @staticmethod
    def extract_stock_price(instrument_identifier):
        # Assuming stock price is the last part of the identifier
        return float(instrument_identifier.split("_")[-1])

    @staticmethod
    def extract_stock_name(instrument_identifier):
        # Assuming stock price is the last part of the identifier
        return float(instrument_identifier.split("_")[-1])
    
    @staticmethod
    def get_live_option_chain(symbols, expiry_dates):
        records = lastquoteoptiongreekschain.find()

        # Filter the data based on symbol and expiry_dates
        filtered_data = [quote for quote in records if
                         symbols in quote["InstrumentIdentifier"] and expiry_dates in quote["InstrumentIdentifier"]]
        return filtered_data

