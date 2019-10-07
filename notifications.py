import requests
import os

def sendPush(message, title, ip):
    data = {
        "token": os.environ["PUSH_TOKEN"],
        "user": os.environ["PUSH_USER_TOKEN"],
        "message": ip + '; ' + message,
        "title": title
    }
    r = requests.post("https://api.pushover.net/1/messages.json", data=data)
    r.status_code # just to actually send request
