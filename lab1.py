import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r)