import urllib3
import json

REGION = 'us-west-2'

http = urllib3.PoolManager()
r = http.request('GET', 'https://ip-ranges.amazonaws.com/ip-ranges.json')
ip_ranges = json.loads(r.data)

ip_prefixes = []
for i in ip_ranges['prefixes']:
    if i['region'] == REGION:
        ip_prefixes.append(i['ip_prefix'])

print(ip_prefixes)