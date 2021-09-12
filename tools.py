import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def cUSD2():
    try:
        url2 = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=iota&vs_currencies=btc&include_24hr_change=true')
        data = url2.json()
        price2 = data["iota"]["btc"]
        change2 = data["iota"]["btc_24h_change"]
       
        return (price2,change2)
    except :
        pass

def cUSD():   
    try:
        url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=iota&vs_currencies=usd&include_24hr_vol=true&include_24hr_change=true')
        data = url.json()
        price = data["iota"]["usd"]
        change24 = data["iota"]["usd_24h_change"]
        vol24 = data["iota"]["usd_24h_vol"] 
        return (price,change24,vol24)
    except :
        pass

def cUSDD(arg):
    arg = arg.upper()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

    parameters = {
        'symbol':f'{arg}',
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '135fd66a-36b1-4179-95a7-58c95b762074',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    try:
        rank = data["data"][f"{arg}"]["cmc_rank"]
        price = data["data"][f"{arg}"]["quote"]["USD"]["price"]
        change1 = data["data"][f"{arg}"]["quote"]["USD"]["percent_change_1h"]
        change24 = data["data"][f"{arg}"]["quote"]["USD"]["percent_change_24h"]    
    except KeyError as err:
        return(err)
    
    return (rank,price,change1,change24)   

def binance(): 
    try:
        url = requests.get('https://api.binance.com/api/v1/ticker/price?symbol=IOTAUSDT')
        data = url.json()
        price = data['price']
        return(float(price))

    except KeyError as err:
        return(err)