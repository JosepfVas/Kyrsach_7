import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

# app.conf.update(
#     broker_url=os.getenv("CELERY_BROKER_URL"),
#     result_backend=os.getenv("CELERY_RESULT_BACKEND"),
#     timezone=os.getenv("TIME_ZONE"),
#     accept_content=["json"],
#     task_serializer="json",
#     result_serializer="json",
#     task_track_started=True,
#     task_time_limit=30 * 60,
#     beat_schedule={
#         "send_message_to_tg_bot": {
#             "task": "habits.tasks.send_message_to_tg_bot",
#             "schedule": 10.0,  # Каждые 10 секунд
#         },
#     },
#     broker_connection_retry_on_startup=True,
# )
