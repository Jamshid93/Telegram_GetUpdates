import requests
r=requests.get('https://randomuser.me/api/')
txt=r.text
data=r.json()

results=data['results'][0]['name']
first_name=results['first']
last_name=results['last']
full_name=first_name+' '+last_name
print(full_name)
