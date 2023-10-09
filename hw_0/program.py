# ModuleNotFoundError: pip install requests
import requests

# AttributeError: request.past -> requests.get
url = 'https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0'
response = requests.get(url)

points = response.json()
# KeyError: points['data'] -> points['dataseries']
# IndexError: add check for n to be less than length of data series
n = 6
if n < len(points['dataseries']):
    wind = points['dataseries'][n]['wind10m']
    print(wind)
else:
    print('n is too big')
