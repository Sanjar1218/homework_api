import requests

dct = [
    {'username': 'Sanjar1218', 'ishere': True}
]

r = requests.get('http://127.0.0.1:8000/check', json=dct)

print(r.json())