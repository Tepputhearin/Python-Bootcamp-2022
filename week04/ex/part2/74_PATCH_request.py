import requests

r = requests.patch("http://localhost:3000/dept/123", json={"deptname": "AI"})

print(r)

print(r.text)