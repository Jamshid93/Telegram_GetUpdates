import requests
import json
currency='RUB'
list_currency=['GBP','EUR','JPY','USD']
payload={'base': currency, 'symbols': list_currency}
r=requests.get('https://api.exchangeratesapi.io/latest',params=payload)
print(r.url)

data=r.json()
res=data['rates']
for k,v in res.items():
     print(f'100 rubles {v*100} {k} in the same !')
