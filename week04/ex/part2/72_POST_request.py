import requests

link = "https://httpbin.org"

myobj = {"somekey": "somevalue"}

x = requests.post(link, json=myobj)

print(x.text)