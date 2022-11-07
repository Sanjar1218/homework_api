import requests

dct = {'date': '17-08-22', 'group': 'Dart2022B'}


r = requests.get('http://127.0.0.1:8000/check', json=dct)

data = r.json()
# print(data)
lst = []
for i in data['data']:
    lst.append({i['full_name']: i['ishere']})
print(lst)