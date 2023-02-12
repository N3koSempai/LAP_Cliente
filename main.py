import requests

json_payload = {'hash': 'ok'}
files = {'files': open('libtest.lat', 'rb') }
r = requests.post('http://127.0.0.1:5000/upload', json=json_payload, files=files)
print(r)
