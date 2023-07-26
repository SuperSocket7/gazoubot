import requests
import random
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('Token')
instance = os.getenv('instance')

filesUrl = f"https://{instance}/api/drive/files"
noteUrl = f"https://{instance}/api/notes/create"
data = {
    'i': token,
    'limit': 100
}


def imgChoice():
    r = requests.post(filesUrl, headers={'Content-Type': 'application/json'}, json=data)
    result = r.json()
    rnd = random.randint(0, len(result))
    imgId = result[rnd]['id']
    return imgId


while True:
    if datetime.now().strftime("%M%S") == "0000":
        notedata = {
            'i': token,
            'mediaIds': [imgChoice()]
        }
        r = requests.post(noteUrl, headers={'Content-Type': 'application/json'}, json=notedata)
        result = r.json()
        print(f"posted: https://{instance}/notes/{result['createdNote']['id']}")
        continue
    else:
        time.sleep(1)
        continue
