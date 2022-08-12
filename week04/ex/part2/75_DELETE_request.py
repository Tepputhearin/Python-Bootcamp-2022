import requests

r = requests.delete("http://localhost:3000/dept", json = {"somekey": "somevalue"})

print(r)
print(r.text)