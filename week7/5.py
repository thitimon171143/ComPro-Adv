import requests
url = 'https://th.wikipedia.org/wiki/รายชื่อเทศบาลตำบลในประเทศไทย'
resq = requests.get(url)
print(resq)
#print(resq.text[:5_000])