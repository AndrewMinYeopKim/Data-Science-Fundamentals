import json
import urllib3

http = urllib3.PoolManager()
query = 'Python'
your_api_key = '33a7e1bcd48d496dbadc1045890f5846'
url = f'https://newsapi.org/v2/everything?q={query}&apiKey={your_api_key}&pageSize=5'
r = http.request('GET', url)
articles = json.loads(r.data.decode('utf-8'))

for a in articles['articles']:
    print(a['title'])
    print(a['publishedAt'])
    print(a['url'])
    print('___')
