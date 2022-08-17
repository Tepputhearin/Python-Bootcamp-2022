import requests
id = input("Id deletetion:")
r = requests.delete(f"http://localhost:3000/dept/{id}")

print(r.status_code)
print(r.text)