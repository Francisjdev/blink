import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
print("FROM:", os.getenv("TWILIO_WHATSAPP_FROM"))
print("TO:", os.getenv("TWILIO_WHATSAPP_TO"))

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_WHATSAPP_FROM")
to_number = os.getenv("TWILIO_WHATSAPP_TO") or ""

client = Client(account_sid, auth_token)


def send_whatsapp_message(message: str):
    client.messages.create(from_=from_number, to=to_number, body=message)
