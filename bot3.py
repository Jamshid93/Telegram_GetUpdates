import requests
response=requests.get('https://randommer.io/')
txt=response.text
data=response.json()

results=data['resluts'][0]['name']
print(results)