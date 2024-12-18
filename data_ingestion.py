import yfinance as yf
from bs4 import BeautifulSoup
import requests
import nltk

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="5y")

def scrape_market_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all('article')
    return [article.get_text() for article in articles]

nltk.download('stopwords')
# Further preprocessing steps(e.g., tokenization)...
