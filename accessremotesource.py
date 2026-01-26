import urllib3

http = urllib3.PoolManager()
r = http.request('GET', 'http://10.4.39.217:8000/sometxt.txt') # sir ablazo PC IP

for i, line in enumerate(r.data.decode('utf-8').split('\n')):
	if line.strip():
	    print(f"Line {i}: {line.strip()}")