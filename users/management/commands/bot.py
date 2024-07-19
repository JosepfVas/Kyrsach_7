import os

from django.core.management import BaseCommand
import requests
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):

    def handle(self, *args, **options):
        # url = f"https://api.telegram.org/bot6523137539:AAGgGoDKzq_EuRotI3xne9vQrBM2TxOi__U/getMe"
        url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_API_KEY')}/getMe"
        response = requests.get(url)
        print(response.json())
