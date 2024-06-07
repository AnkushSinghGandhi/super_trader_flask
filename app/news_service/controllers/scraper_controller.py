from models.scraper import Scraper

class ScraperController:
    def __init__(self):
        self.scraper = Scraper()

    def get_news(self, categories=None, queries=None):
        pages_to_scrape = []

        if categories:
            pages_to_scrape += [self.scraper.build_url(category=cat) for cat in categories]

        if queries:
            pages_to_scrape += [self.scraper.build_url(query=query) for query in queries]

        news = self.scraper.scrape_news(pages_to_scrape)
        return news
