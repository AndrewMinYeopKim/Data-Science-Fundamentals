import requests
import sys
import json
import csv


ip = sys.argv[1] # 10.4.39.217:8000
index = int(sys.argv[2])
r = requests.get(f'http://{ip}/topics.txt')
topics = r.text.split('\n')
print(topics[index-1])

query = topics[index-1]
params = {
    'q': query,
    'apiKey': '33a7e1bcd48d496dbadc1045890f5846',
    'pageSize': 40
}

r = requests.get('https://newsapi.org/v2/everything', params)
articles = json.loads(r.text)

with open(f"Arocena_Kim_Villarente_{query}.csv", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = "source author title url publishedAt description".split()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    row = {fieldname: '' for fieldname in fieldnames}

    for a in articles['articles']:
        row['source'] = a['source']['name']
        row['author'] = a['author']
        row['title'] = a['title']
        row['url'] = a['url']
        row['publishedAt'] = a['publishedAt']
        row['description'] = a['description']
        writer.writerow(row)