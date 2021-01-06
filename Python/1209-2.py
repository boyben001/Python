import requests
import pprint
'''
r = requests.get('http://google.com.tw')
pprint.pprint(r.text)
'''
api_url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010'
weather_data = requests.get(api_url).json()
pprint.pprint(weather_data)
