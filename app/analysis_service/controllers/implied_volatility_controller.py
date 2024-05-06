from flask import jsonify
from models.last_quote_option_greeks import QuoteOptionGreeksModel


class ImpliedVolatilityController:
    @staticmethod
    def get_iv_chart():
        data = QuoteOptionGreeksModel.get_iv_data()

        iv_chart = []

        for item in data:
            # Extract necessary data from the item dictionary
            # Close price and price change percentage are not included in the provided data
            # For demonstration purposes, let's assume some sample data
            close_price = 1000
            price_change_percentage = 5

            # Calculate RV 30
            rv_30 = price_change_percentage * 30 ** 0.5

            # Calculate RV 10
            rv_10 = price_change_percentage * 10 ** 0.5

            # Calculate IV-RV Spread (IV-RV30)
            iv_rv_spread = rv_30 + 10

            # Calculate IV Percentile (implement your specific logic here based on Excel formula)

            # Create the IV chart dictionary for the current item
            iv_chart_item = {
                'Token': item['Token'],
                'RV 30': rv_30,
                'RV 10': rv_10,
                'IV-RV Spread': iv_rv_spread,
                'IV Percentile': None  # Replace None with the calculated IV Percentile value
            }

            iv_chart.append(iv_chart_item)

        return jsonify(iv_chart)

