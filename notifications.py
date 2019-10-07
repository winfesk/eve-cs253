import requests
import os

def sendPush(message):
    data = {
        "token": os.environ["PUSH_TOKEN"],
        "user": os.environ["PUSH_USER_TOKEN"],
        "message": message
    }
    r = requests.post("https://api.pushover.net/1/messages.json", data=data)
    r.status_code # just to actually send request
