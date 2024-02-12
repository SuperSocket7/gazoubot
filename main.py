import requests
import random
import json
import time as timer
from datetime import datetime

with open("setting.json") as f:
    setting = json.loads(f.read())
token = setting['Token']
instance = setting['instance']
icon = setting['icon']
# MisskeyはたまにAPIエンドポイントが変わりやがるので
filesUrl = f"https://{instance}/api/drive/files"
noteUrl = f"https://{instance}/api/notes/create"


def icon_remove(imglist: list):
    for img in imglist:
        if img["name"] == icon:
            imglist.remove(img)
    return imglist


def img_fetch():
    r = requests.post(filesUrl, headers={'Content-Type': 'application/json'}, json={'i': token, 'limit': 100})
    files = r.json()
    while True:
        if len(r.json()) == 100:
            r = requests.post(filesUrl, headers={'Content-Type': 'application/json'}, json={'i': token, 'limit': 100, 'untilId': r.json()[99]['id']})
            files += r.json()
        else:
            break
    files = icon_remove(files)
    return files


def img_choice(imglist: list):
    img = random.choice(imglist)
    return img


imglist = img_fetch()
# ループ部分、TMKありがと
prevTime = 0
while True:
    nInterval = 10
    time = int(datetime.now().strftime("%M")) * 60 + int(datetime.now().strftime("%S"))
    if prevTime > time:
        notedata = {
            'i': token,
            'mediaIds': [img_choice(imglist)["id"]]
        }
        result = requests.post(noteUrl, headers={'Content-Type': 'application/json'}, json=notedata).json()
        print(f"posted: https://{instance}/notes/{result['createdNote']['id']}")
    prevTime = time
    timer.sleep(nInterval)
    continue
