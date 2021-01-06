import requests
import bs4

url = "https://www.mymusic.net.tw/ux/w/search/"
search_name = "你好不好"

res = requests.get(url + search_name)

soup = bs4.BeautifulSoup(res.text, 'html.parser')
