import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = 'https://finance.yahoo.com'

class Scraper:
    def __init__(self):
        self.base_url = BASE_URL

    def build_url(self, category=None, query=None):
        if category:
            return f'{self.base_url}/{category}/'
        if query:
            return f'{self.base_url}/search?p={query}'
        return self.base_url

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_news(self, page_content):
        soup = BeautifulSoup(page_content, 'html.parser')
        news_items = []

        news_container = soup.find('ul', class_='My(0) P(0) Wow(bw) Ov(h) List(n)')
        if not news_container:
            return news_items

        for item in news_container.find_all('li'):
            headline = item.find('h3').get_text() if item.find('h3') else None
            link = item.find('a')['href'] if item.find('a') else None
            summary = item.find('p').get_text() if item.find('p') else None

            if headline and link:
                news_items.append({
                    'headline': headline,
                    'link': self.base_url + link,
                    'summary': summary
                })
        return news_items

    def scrape_news(self, pages):
        news = []
        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(self.fetch_page, url): url for url in pages}

            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    page_content = future.result()
                    if page_content:
                        news.extend(self.parse_news(page_content))
                except Exception as e:
                    print(f"Error processing {url}: {e}")
        return news
