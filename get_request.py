import requests

r = requests.post('https://www.mangatail.me/')
print(r.status_code)
