# Accessing data from API (practice activity)

# Instructions
# Create a python script that accesses the back end / api of newsapi.org and extracts the following details for 20 article instances:
# 1.	source (the name, not id)
# 2.	author
# 3.	title
# 4.	url
# 5.	publishedAt
# Once the 20 articles' details are gathered write/save these in a csv named: yourquery.csv - where yourquery - is the query string returned by the script above. Gather csvs for the following query/topics: Trump, Philippines, China, Cats, Boruto, Naruto, DataScience, Computing, Mindanao.

import requests
import json
import csv

queries = ['Trump', 'Philippines', 'China', 'Cats', 'Boruto', 'Naruto', 'DataScience', 'Computing', 'Mindanao']

for query in queries:
    params = {
        'q' : query,
        'apiKey' : '33a7e1bcd48d496dbadc1045890f5846',
        'pageSize' : 20
    }

    request = requests.get('https://newsapi.org/v2/everything', params) # from import requests 
    articles = json.loads(request.text) # dictionary of articles converted from api response

    with open(f"{query}.csv", 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = "source author title url publishedAt".split()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        row = {fieldname: '' for fieldname in fieldnames}
        
        for article in articles['articles']:
            row['source'] = article['source']['name']
            row['author'] = article['author']
            row['title'] = article['title']
            row['url'] = article['url']
            row['publishedAt'] = article['publishedAt']
            writer.writerow(row)
            