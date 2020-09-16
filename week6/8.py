import requests

response = requests.get('https://api.exchangeratesapi.io/latest?base=THB')
exchange_rates = eval(response.text)["rates"]

print('Exchange Calculator')
rate = input('Currency : ')
money = int(input('Money : '))
print(exchange_rates[rate]*money)