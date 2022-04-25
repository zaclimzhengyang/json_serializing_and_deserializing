import json
from urllib.request import urlopen

# https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json
# was initially used but yahoo finance stopped their webservice api service to public
with urlopen("https://sg.yahoo.com/?p=us") as response:
    source = response.read()

print(source)

#data = json.loads(source)

#print(json.dumps(data, indent=2))
'''
usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/INR']))'''