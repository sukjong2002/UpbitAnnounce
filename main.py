# -*- coding: utf-8 -*-
import requests
import time

from sendMsg import send

url = "https://api-manager.upbit.com/api/v1/notices?page="+str(1)+"&per_page="+str(20)+"&thread_name="+"general"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}

def getLatest():
    cont = requests.get(url, headers=headers)
    json = cont.json()

    return json['data']['list'][0]

try:
    lastTitle = getLatest()['title']
    #lastTitle = 'kd'
    while True:
        time.sleep(5)
        temp = getLatest()
        if lastTitle != temp['title']:
            send(temp)

except Exception:
    raise    

