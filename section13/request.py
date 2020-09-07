import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(r)

payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request(
    'http://httpbin.org/get', data=payload, method='POST')
