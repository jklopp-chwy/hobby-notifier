import os
import twilio
from twilio.rest import Client
import config

# Your Account SID from twilio.com/console
account_sid = config.twilio["account_sid"]
# Your Auth Token from twilio.com/console
auth_token  = config.twilio["auth_token"]
#from phone number
sending_number = config.twilio["twilio_phone_number"]
#your phone number
my_phone_number = config.twilio["my_phone_number"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=my_phone_number, 
    from_=sending_number,
    body="Hello from Python!")

print(message.sid)