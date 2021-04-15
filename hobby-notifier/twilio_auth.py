import os
import twilio
from twilio.rest import Client
import config

account_sid = config.twilio["account_sid"]
auth_token  = config.twilio["auth_token"]
sending_number = config.twilio["twilio_phone_number"]
my_phone_number = config.twilio["my_phone_number"]

client = Client(account_sid, auth_token)

def sendSms(message):
    message = client.messages.create(
                    to=my_phone_number, 
                    from_=sending_number,
                    body=message)