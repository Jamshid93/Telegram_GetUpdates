import requests
import json
r=requests.get('https://api.telegram.org/bot1203017099:AAHQRZKDnyNGfWceg2kyRFNB274TjNl5FuI/getUpdates')
#print(r.url)
data=r.json()
newmassage=data['result'][0]['update_id']
frome=data['result'][0]['message']['from']
chat=data['result'][0]['message']['chat']
#print(data)
print(newmassage)
print(frome)
print(chat)