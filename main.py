import os
from pprint import pprint
import json
import requests
token=os.environ['token']
def update():
    url=f'https://api.telegram.org/bot{token}/getUpdates'

    r=requests.get(url)
    data=r.json()['result']
    update_id=data[-1]['update_id']
    chat_id=data[-1]['message']['chat']['id']
    text=data[-1]['text']
    inform=[update_id,chat_id,text]
    return inform


last_update_id=None
while True:
    inform=update()
    update_id=inform[0]
    if last_update_id!=update_id:
        last_update_id=update_id
