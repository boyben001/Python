from pytube import YouTube
from bs4 import BeautifulSoup
import re
import requests
import requests.packages.urllib3
import urllib3.request
import json
import pprint
requests.packages.urllib3.disable_warnings()


songElect = []
languageElect = []
typeElect = []
artistElect = []


# def showRandomSong():


# def songRecord():

print("輸入歌手or歌名 : ", end='')
search = str(input())
url = ('https://www.youtube.com/results?search_query=' + search)
song = 'https://www.youtube.com/watch?v=3AtDnEC4zak&ab_channel=CharliePuth'
html_data = requests.get(song)
soup = BeautifulSoup(html_data.text, 'html.parser')
