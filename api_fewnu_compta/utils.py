from django.conf import settings
import os

import twilio
import twilio.rest
from twilio.rest import Client

def send_twilio_message(to_number, body):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    return client.messages.create(
    from_='+18146377359',
    body='hello',
    to='+221764553046'
    )

# print(client.sid)
    

