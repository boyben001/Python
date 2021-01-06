#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
yahoo_tech_news_xml = requests.get('https://tw.news.yahoo.com/rss/technology')
soup = BeautifulSoup(yahoo_tech_news_xml.text, "html.parser")
type(soup)
soup.findAll('item')
for news in soup.findAll('item'):
    print(news.title)


