import requests

print(requests.__version__)

r = requests.get("http://www.google.com")
print(r)


r = requests.get("https://raw.githubusercontent.com/naviza/CMPUT404_Lab/main/lab1.py", allow_redirects=True)
open('lab1.py', 'wb').write(r.content)
