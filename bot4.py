import requests
import json
currency='USD'
list_currency=['GBP','CAD','KRW','RUB']
payload={'base': currency, 'symbols': list_currency[:2]}
r=requests.get('https://api.exchangeratesapi.io/latest',params=payload)
print(r.url)

data=r.json()
print(data)