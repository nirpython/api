
import requests
res = requests.get('http://v4.ident.me/')
print(res.content)
