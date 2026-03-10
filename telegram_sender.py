import requests
import os

TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_pdf():

    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"

    files = {
        "document": open("daily_news.pdf","rb")
    }

    data = {
        "chat_id": CHAT_ID
    }

    requests.post(url, data=data, files=files)