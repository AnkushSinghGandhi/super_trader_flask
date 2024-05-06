## get_last_quote_Array.json
## futures_list = json_data[0]['Result']
from flask import jsonify, request
from models.last_quote_array import LastQuoteArrayModel


class FutureDashboardController:
    @staticmethod
    def get_future_dashboard_data():
        status = request.args.get('status')

        # Fetch data from MongoDB collection
        futures_list = LastQuoteArrayModel.get_last_quote_array()

        if status.lower() == 'price_change':
            sorted_futures = sorted(futures_list, key=lambda x: x.get('PriceChangePercentage', 0), reverse=True)

            top_10_highest = sorted_futures[:10]
            top_10_lowest = sorted_futures[-10:]

            response = {
                'Message': 'Success',
                'status': 200,
                'data': {
                    'top_10_highest': top_10_highest,
                    'top_10_lowest': top_10_lowest
                }
            }

            return jsonify(response)

        if status == 'oi_change':
            sorted_futures = sorted(futures_list, key=lambda x: x.get('OpenInterestChange', 0), reverse=True)
            top_10_highest = sorted_futures[:10]

            response = {
                'Message': 'Success',
                'status': 200,
                'data': top_10_highest
            }

            return jsonify(response)

        if status.lower() == 'long_buildup':
            sorted_futures = sorted(futures_list,
                                    key=lambda x: (x.get('OpenInterestChange', 0), x.get('PriceChangePercentage', 0)),
                                    reverse=True)

            top_10 = sorted_futures[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10': top_10
                }
            }

            return jsonify(response)

        if status.lower() == 'short_buildup':
            sorted_futures = sorted(futures_list,
                                    key=lambda x: (x.get('OpenInterestChange', 0), x.get('PriceChangePercentage', 0)))

            top_10 = sorted_futures[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10': top_10
                }
            }

            return jsonify(response)

        if status.lower() == 'short_covering':
            sorted_futures = sorted(futures_list,
                                    key=lambda x: (x.get('OpenInterestChange', 0), x.get('PriceChangePercentage', 0)),
                                    reverse=True)

            top_10 = sorted_futures[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10': top_10
                }
            }

            return jsonify(response)

        if status.lower() == 'long_unwinding':
            sorted_futures = sorted(futures_list,
                                    key=lambda x: (x.get('OpenInterestChange', 0), x.get('PriceChangePercentage', 0)))

            top_10 = sorted_futures[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10': top_10
                }
            }

            return jsonify(response)

        if status.lower() == 'highest_turnover':
            sorted_futures = sorted(futures_list, key=lambda x: x.get('Turnover', 0), reverse=True)

            top_10 = sorted_futures[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10': top_10
                }
            }

            return jsonify(response)

        if status.lower() == 'iv_change':
            sorted_futures_highest = sorted(futures_list, key=lambda x: x.get('IVChangePercentage', 0), reverse=True)
            sorted_futures_lowest = sorted(futures_list, key=lambda x: x.get('IVChangePercentage', 0))

            top_10_highest = sorted_futures_highest[:10]
            top_10_lowest = sorted_futures_lowest[:10]

            response = {
                'message': 'Success',
                'status': 200,
                'data': {
                    'top_10_highest': top_10_highest,
                    'top_10_lowest': top_10_lowest
                }
            }

            return jsonify(response)

        response = {
            'message': 'Invalid status',
            'status': 400,
            'data': None
        }

        return jsonify(response)