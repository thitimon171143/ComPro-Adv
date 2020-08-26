import requests

response = requests.get('https://restcountries.eu/rest/v2/regionalbloc/ASEAN')
data = response.json()
print(type(data))
print(data)
'''asean_name = eval(response.text)["name"]
asean_population = eval(response.text)["population"]
asean_area = eval(response.text)["area"]'''

'''print(asean_name['name'])
print(asean_population['population'])
print(asean_area['area'])'''