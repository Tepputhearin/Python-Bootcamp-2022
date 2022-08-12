import requests

link = "http://localhost:3000/dept"

x = requests.get(link)
print(x.text)
