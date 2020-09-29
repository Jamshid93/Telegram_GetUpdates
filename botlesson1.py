import requests
response=requests.get('https://randomuser.me/api/')
print(response.status_code)
if response.status_code==200:
    print('Succes!')
elif response.status_code==404:
    print('Not Found.')
print(response.content)
#print(response.text)
#print(response.json())