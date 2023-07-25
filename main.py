import requests
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('Token')
instance = os.getenv('instance')

uploadurl = f"https://{instance}/api/drive/files"
noteurl = f"https://{instance}/api/notes/create"
header = {
    'Content-Type': 'application/json'
}
data = {
    'i': token,
    'limit': 100
}

def imgChoice():
    r = requests.post(uploadurl, headers=header, json=data)
    result = r.json()
    rnd = random.randint(0, 58)
    imgId = result[rnd]['id']
    return imgId


while True:
    notedata = {
        'i': token,
        'mediaIds': [imgChoice()]
    }
    r = requests.post(noteurl, headers=header, json=notedata)
    result = r.json()
    print(f"posted: https://{instance}/notes/{result['createdNote']['id']}")
    time.sleep(60 * 60)
    continue