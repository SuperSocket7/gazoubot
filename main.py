import requests
import random
import time as t
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('Token')
instance = os.getenv('instance')
icon = os.getenv('icon')

filesUrl = f"https://{instance}/api/drive/files"
noteUrl = f"https://{instance}/api/notes/create"


def imgChoice():
    r = requests.post(filesUrl, headers={'Content-Type': 'application/json'}, json={'i': token, 'limit': 100})
    dicFiles = r.json()
    tmpFiles = dicFiles
    while True:
        if len(tmpFiles) == 100:
            r = requests.post(filesUrl, headers={'Content-Type': 'application/json'}, json={'i': token, 'limit': 100, 'untilId': tmpFiles[99]['id']})
            tmpFiles = r.json()
            dicFiles += r.json()
        else:
            break
    while True:
        rnd = random.randint(0, len(dicFiles))
        if dicFiles[rnd]['name'] == icon:
            del dicFiles[rnd]
            continue
        else:
            imgId = dicFiles[rnd]['id']
            return imgId


# ループ部分、TMKありがと
prevTime = 0
while True:
    nInterval = 10
    time = int(datetime.now().strftime("%M")) * 60 + int(datetime.now().strftime("%S"))
    if prevTime > time:
        notedata = {
            'i': token,
            'mediaIds': [imgChoice()]
        }
        try:
            r = requests.post(noteUrl, headers={'Content-Type': 'application/json'}, json=notedata)
        except requests.Timeout:
            print(f"error: サーバーに接続できませんでした")
            continue
        result = r.json()
        print(f"posted: https://{instance}/notes/{result['createdNote']['id']}")
    prevTime = time
    t.sleep(nInterval)
    continue
