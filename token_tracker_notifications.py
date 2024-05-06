import requests     
from twilio.rest import Client
import time 
import os

api_url = 'https://api.dexscreener.com/latest/dex/pairs/solana/X131b3frGn4b8ue51EyvrnzWuTuBGoM93uRYrNteEFy'

# twilio config
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')
recipient_number = os.getenv('RECIPIENT_NUMBER')

client = Client(account_sid, auth_token)


def get_hammy_price():
    response = requests.get(api_url)
    data = response.json()
    if 'pairs' in data and len(data['pairs']) > 0:
        price_usd = data['pairs'][0].get('priceUsd',0)
        return float(price_usd)
    else:
        return 0

def send_sms(price):
    message = client.messages.create( 
        from_ = twilio_number,
        body = f'Yo! HAMMY price is now {price} USD',
        to = recipient_number
    )
         
    print(f'SMS sent: {message.sid}')
 
def get_thresholds(current_price, increment = 0.005):
     return [current_price - increment, current_price + increment]
    
def has_crossed_threshold(current_price, thresholds): 
    return current_price > thresholds[1] or current_price < thresholds[0]
   
last_price = get_hammy_price()  
if last_price is not None:
    thresholds = get_thresholds(last_price)

while True:
    current_price = get_hammy_price()
    if current_price is not None and last_price is not None:
        if has_crossed_threshold(current_price, thresholds):
            send_sms(current_price)
            last_price = current_price
            thresholds = get_thresholds(current_price)   
    else:
        print('Cooked it bruh.')
    time.sleep(120) 
    
    