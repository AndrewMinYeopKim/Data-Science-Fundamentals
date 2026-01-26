import requests

r = requests.get('http://10.4.39.217:8000/sometxt.txt')

r.encoding = 'utf-8' # will decode to unicode so output wont be jibberish
for i, line in enumerate(r.text.split('\n')):
    if line.strip():
        print(f"Line {i}: {line.strip()}")