import requests

r = requests.put("https://httpbin.org / put", data ={"key":"value"})

print(r.text)
