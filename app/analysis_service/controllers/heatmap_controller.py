from flask import jsonify, request
from models.last_quote_array import LastQuoteArrayModel


class HeatMapController:
    @staticmethod
    def get_heat_map():
        last_quote_array_data = LastQuoteArrayModel.get_last_quote_array()

        # Constants
        nifty50_constituents = [
            'AdaniPorts-I',
            'Adani-Enterprises-I',
            'Apollo-Hospitals-I',
            'Axis-Bank-I',
            'Hero-MotoCorp',
            'ICICI-Bank',
            'ITC',
            'Infosys',
            'Indusind-Bank',
            'JSW-Steel',
            'Kotak-Mahindra-Bank',
            'Larsen-&-Toubro',
            'LTIMindtree',
            'Mahindra-and-Mahindra',
            'Maruti-Suzuki',
            'Nestle',
            'Oil-and-Natural-Gas-Corporation',
            'NTPC',
            'Power-Grid-Corporation-of-India',
            'Reliance-Industries',
            'State-Bank-of-India',
            'SBI-Life-Insurance-Company',
            'Sun-Pharmaceutical-Industries',
            'TATASTEEL',
            'Tata-Consumer-Products',
            'Tata-Motors',
            'TCS',
            'TECHM',
            'Titan-Company',
            'UPL',
            'ULTRACEMCO',
            'Wipro',
        ]
        banknifty_constituents = [
            'HDFC-Bank',
            'ICICI-Bank',
            'State-Bank-of-India-(SBI)',
            'Kotak-Bank',
            'Axis-Bank',
            'IndusInd-Bank',
            'Punjab-National-Bank',
            'Bank-of-Baroda',
            'Federal-Bank',
            'IDFC-First-Bank',
            'RBL-Bank',
            'AUBank'
        ]

        instrument_server_time = {}

        for quote in last_quote_array_data:
            InstrumentIdentifier = quote["InstrumentIdentifier"]
            server_time = quote["ServerTime"]

            if InstrumentIdentifier in instrument_server_time:
                if server_time > instrument_server_time[InstrumentIdentifier]:
                    instrument_server_time[InstrumentIdentifier] = server_time
            else:
                instrument_server_time[InstrumentIdentifier] = server_time

        results_nifty50 = []
        results_banknifty = []
        results_fno = []

        for quote2 in last_quote_array_data:
            InstrumentIdentifier = quote2["InstrumentIdentifier"]
            ltp = quote2["LastTradePrice"]
            price_percentage_change = quote2["PriceChangePercentage"]
            server_time = quote2["ServerTime"]

            if server_time == instrument_server_time[InstrumentIdentifier]:
                if any(value.lower() in InstrumentIdentifier.lower() for value in nifty50_constituents):
                    results_nifty50.append({
                        'InstrumentIdentifier': InstrumentIdentifier,
                        'LTP': ltp,
                        'PricePercentageChange': price_percentage_change
                    })

                if any(value.lower() in InstrumentIdentifier.lower() for value in banknifty_constituents):
                    results_banknifty.append({
                        'InstrumentIdentifier': InstrumentIdentifier,
                        'LTP': ltp,
                        'PricePercentageChange': price_percentage_change
                    })

                results_fno.append({
                    'InstrumentIdentifier': InstrumentIdentifier,
                    'LTP': ltp,
                    'PricePercentageChange': price_percentage_change
                })

        return jsonify({
            'Nifty50': results_nifty50,
            'Banknifty': results_banknifty,
            'FNO': results_fno
        })
