import requests
from config import settings


def send_telegram_message(telegram_id, message):
    """ Функция интеграции с Телеграмом """

    print(f"Отправка напоминание для: {telegram_id}: {message}")
    params = {
        "text": message,
        "chat_id": telegram_id,
    }
    response = requests.post(
        f"{settings.TELEGRAM_URL}{settings.TELEGRAM_BOT_API_KEY}/sendMessage",
        params=params,
    )
    print(response.status_code)
