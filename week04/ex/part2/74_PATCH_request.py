import requests

r = requests.patch("http://localhost:3000/dept", json={"somekey": "somevaluea"})

print(r)

print(r.text)