import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_WHATSAPP_FROM")
to_number = os.getenv("TWILIO_WHATSAPP_TO")

client = Client(account_sid, auth_token)


def send_whatsapp_message(message: str):
    client.messages.create(from_=from_number, to=to_number, body=message)
