import requests

r = requests.put("http://localhost:3000/dept", json={"somekey": "somevalues", "id":125})

print(r)
print(r.text)
