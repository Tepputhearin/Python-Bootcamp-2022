import requests

link = "http://maps.googleapis.com/maps/api/geocode/json"

x = requests.get(link)
print(x.text)
