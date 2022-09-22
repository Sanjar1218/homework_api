import requests

dct = [
    {'date': '15-07-22'},
    {'date': '18-07-22'}
]

r = requests.get('http://127.0.0.1:8000/check', json=dct)

print(r.json())