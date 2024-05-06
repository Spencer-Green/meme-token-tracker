import requests     
from twilio.rest import Client

api_url = 'https://api.dexscreener.com/latest/dex/pairs/solana/X131b3frGn4b8ue51EyvrnzWuTuBGoM93uRYrNteEFy'

def get_hammy_price():
    response = requests.get(api_url)
    data = response.json()
    if 'pairs' in data and len(data['pairs']) > 0:
        price_usd = data['pairs'][0].get('priceUsd', 0)
        return float(price_usd)
    else:
        return None


current_price = get_hammy_price()
if current_price is not None:
    print(f"The current price of HAMMY is: ${current_price}")
else:
    print("Failed to fetch the current price of HAMMY.")