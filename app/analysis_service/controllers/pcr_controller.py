from flask import jsonify
from app.shared.models.last_quote_option_greek_chain import LastQuoteOptionChainModel


class PcrController:
    @staticmethod
    def get_pcr_data():
        option_database_data = LastQuoteOptionChainModel.get_option_greek_chain()

        stock_data2 = {}
        for option in option_database_data:
            instrument_identifier = option["InstrumentIdentifier"]
            stock_name = LastQuoteOptionChainModel.extract_stock_name(instrument_identifier)
            date = LastQuoteOptionChainModel.extract_date(instrument_identifier)

            if stock_name not in stock_data2:
                stock_data2[stock_name] = []

            total_call_volume = 0
            total_put_volume = 0
            total_call_oi = 0
            total_put_oi = 0

            if stock_name in stock_data2:
                for option_data in stock_data2[stock_name]:
                    total_call_volume += option_data.get("TotalCallVolume", 0)
                    total_put_volume += option_data.get("TotalPutVolume", 0)
                    total_call_oi += option_data.get("TotalCallOI", 0)
                    total_put_oi += option_data.get("TotalPutOI", 0)

            if "CE" in instrument_identifier:
                total_call_volume += option["Value"]
                total_call_oi += option["OpenInterest"]
            elif "PE" in instrument_identifier:
                total_put_volume += option["Value"]
                total_put_oi += option["OpenInterest"]

            stock_data2[stock_name].append({
                "date": date,
                "volumepcr": total_put_volume,
                "oipcr": total_put_oi,
                "stockprice": LastQuoteOptionChainModel.extract_stock_price(instrument_identifier)
            })

        result = []
        for stock_name, data in stock_data2.items():
            result.append({
                "stock_name": stock_name,
                "data": data
            })

        return jsonify(result)