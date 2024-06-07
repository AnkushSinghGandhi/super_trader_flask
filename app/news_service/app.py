from flask import Flask, request, jsonify
from controllers.scraper_controller import ScraperController

app = Flask(__name__)
scraper_controller = ScraperController()

@app.route('/api/news', methods=['GET'])
def get_news():
    categories = request.args.getlist('category')
    queries = request.args.getlist('query')

    news = scraper_controller.get_news(categories, queries)
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
