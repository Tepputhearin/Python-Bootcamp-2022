import requests

r = requests.put("http://localhost:3000/dept/126", json={"somekey": "somevalues123"})

print(r)
print(r.text)
