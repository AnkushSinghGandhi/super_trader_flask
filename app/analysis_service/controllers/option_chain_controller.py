from flask import jsonify, request
from models.last_quote_option_greek_chain import LastQuoteOptionChainModel

class OptionChainController:
    @staticmethod
    def get_option_chain():
        symbols = 'AAPL'#request.args.get('symbols')
        expiry_dates = '2022-04-29' #request.args.get('expiry_dates')

        # Get live option chain data from the model
        option_chain_data = LastQuoteOptionChainModel.get_live_option_chain(symbols, expiry_dates)

        # Prepare the response data
        results = []
        for quote in option_chain_data:
            result = {
                "InstrumentIdentifier": quote["InstrumentIdentifier"],
                "PriceChangePercentage": quote["PriceChangePercentage"],
                "OpenInterestChange": quote["OpenInterestChange"],
                "BuyPrice": quote["BuyPrice"],
                "PriceChange": quote["PriceChange"],
                "LastTradePrice": quote["LastTradePrice"],
                "BuyQty": quote["BuyQty"],
                "SellPrice": quote["SellPrice"],
                "SellQty": quote["SellQty"],
                "Value": quote["Value"],
                "OpenInterest": quote["OpenInterest"],
                "IV": quote["IV"],
                "Theta": quote["Theta"],
                "Delta": quote["Delta"],
                "Vega": quote["Vega"],
                "Gamma": quote["Gamma"],
                "IVVwap": quote["IVVwap"],
                "Vanna": quote["Vanna"],
                "Charm": quote["Charm"],
                "Speed": quote["Speed"],
                "Zomma": quote["Zomma"],
                "Color": quote["Color"],
                "DTR": quote["DTR"],
                "Veta": quote["Veta"],
                "Volga": quote["Volga"],
                "ThetaGammaRatio": quote["ThetaGammaRatio"],
                "ThetaVegaRatio": quote["ThetaVegaRatio"],
            }
            results.append(result)

        # Return the filtered data as a response
        return jsonify({
            "Message": "Live Option Chain",
            "data": results,
            "status": 200
        })
