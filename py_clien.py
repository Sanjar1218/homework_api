import requests

dct = {
    'first_name': 'Sanjarbek',
    'last_name': 'Saidov',
    'username': 'Sanjar1218',
    'phone': 907060973,
}

r = requests.post('http://127.0.0.1:8000/createUser', json=dct)

print(r.json())