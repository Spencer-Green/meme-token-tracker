from twilio.rest import Client
import os

def send_test_sms():
    account_sid = os.getenv('ACCOUNT_SID')
    auth_token = os.getenv('AUTH_TOKEN')   
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv('TWILIO_NUMBER'),  
        body='Hello! This is a test message from your script.',
        to=os.getenv('RECIPIENT_NUMBER')
    )
    print(f"Test SMS sent: {message.sid}")


send_test_sms()
