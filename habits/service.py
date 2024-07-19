import requests
from config import settings


def send_telegram_message(telegram_id, message):
    print(f"Отправка напоминание для: {telegram_id}: {message}")
    params = {
        "text": message,
        "chat_id": telegram_id,
    }
    # response = requests.post(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_API_KEY}/sendMessage", params=params)
    response = requests.post(
        f"https://api.telegram.org/bot6523137539:AAGgGoDKzq_EuRotI3xne9vQrBM2TxOi__U/sendMessage",
        params=params,
    )
    print(response.status_code)
