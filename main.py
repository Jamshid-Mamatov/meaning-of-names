import os

import json

import requests


token=os.environ['token']
def update():
    url=f'https://api.telegram.org/bot{token}/getUpdates'

    r=requests.get(url)
    data=r.json()['result']
    
    chat_id=data[-1]['message']['chat']['id']
    text=data[-1]['message']['text']
    inform=[chat_id,text]
    return inform

def update_id():
    url=f'https://api.telegram.org/bot{token}/getUpdates'

    r=requests.get(url)
    data=r.json()['result']
    update_id=data[-1]['update_id']
    return update_id


def get_name_mean(name):
    url=f'https://ismlar.com/name/{name}'
    r=requests.get(url)
    
       
    data=str(r.text)
    response=data.find(name)
    if response!=-1:

        ind =data.find("<title>")
        ind_start=data.find('content=',ind)
        ind_start=ind_start+len('content=')
        ind_end=data.find('>',ind_start)
        name_mean=data[ind_start:ind_end]
    else:
        name_mean="name not found"   
    
    return name_mean
    


def sendMsg():
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    inform=update()
    text=get_name_mean(inform[1])
    chat_id=inform[0]
    payload={
        'chat_id':chat_id,
        'text':text
    }

    r=requests.get(url,params=payload)
        

last_update_id=None
while True:
    new_update_id=update_id()
    
    if last_update_id!=new_update_id:
        last_update_id=new_update_id
        
        sendMsg()

