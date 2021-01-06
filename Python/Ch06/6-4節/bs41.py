#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
html_data = requests.get('http://tw.yahoo.com')
soup = BeautifulSoup(html_data.text, "html.parser")
soup.title
