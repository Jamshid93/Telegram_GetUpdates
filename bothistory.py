import requests
import json
currency='USD'
list_currency=['RUB']
s=str('2018-01-01')
e=str('2019-01-01')
payload={'base': currency, 'symbols': list_currency, 'start_at':s, 'end_at':e}
r=requests.get('https://api.exchangeratesapi.io/history?',params=payload)
print(r.url)

data=r.json()
print(data)

