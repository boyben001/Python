#pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
game_ranking_html = requests.get('https://acg.gamer.com.tw/billboard.php?t=2&p=Android')
game_ranking_html.encoding = 'UTF-8'
soup = BeautifulSoup(game_ranking_html.text, "html.parser")
#find no.1 game'name
soup.find(class_='ACG-mainbox1').find(class_='ACG-maintitle').find('a').string
#find others by ranking
for game in soup.findAll(class_='ACG-mainbox1'):
    print(game.find(class_='ACG-mainumber').string + ' ' + game.find(class_='ACG-maintitle').find('a').string)





