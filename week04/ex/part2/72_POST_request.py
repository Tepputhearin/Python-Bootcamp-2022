import requests

link = "http://localhost:3000/dept"

myobj = {"somekey": "somevalue"}

x = requests.post(link, json=myobj)

print(x.text)