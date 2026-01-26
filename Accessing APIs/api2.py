import requests
import json
import csv

query = 'Python'
params = {
    'q': query,
    'apiKey': '33a7e1bcd48d496dbadc1045890f5846',
    'pageSize': 5
}

r = requests.get('https://newsapi.org/v2/everything', params)
articles = json.loads(r.text)

with open(f"{query}.csv", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = "source author title url publishedAt".split()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    row = {fieldname: '' for fieldname in fieldnames}

    for a in articles['articles']:
        row['source'] = a['source']['name']
        row['author'] = a['author']
        row['title'] = a['title']
        row['url'] = a['url']
        row['publishedAt'] = a['publishedAt']
        writer.writerow(row)


