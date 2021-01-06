import requests
from bs4 import BeautifulSoup
html_data = requests.get('https://udn.com/news/index')
soup = BeautifulSoup(html_data.text,"html.parser")
soup.title
