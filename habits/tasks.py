from django.utils import timezone
from datetime import datetime, timedelta
from habits.models import Habit
from habits.service import send_telegram_message


def send_message_to_tg_bot():
    """Функция отправки уведомления о привычке"""
    habits = Habit.objects.all()
    now = timezone.localtime(
        timezone.now()
    )

    for habit in habits:
        if habit.time:
            habit_time = habit.time

            if now.time() >= habit_time:
                last_sent = habit.last_sent
                if not last_sent or now - last_sent >= timedelta(days=habit.periodic):
                    message = (
                        f"Не забудь про привычку '{habit.action}' в {habit_time.strftime('%H:%M')}\n"
                        f"После этого можно:\n"
                        f"{habit.linked_habit.action if habit.linked_habit else habit.reward}"
                    )

                    if habit.owner and habit.owner.telegram_id:
                        try:
                            send_telegram_message(
                                telegram_id=habit.owner.telegram_id, message=message
                            )
                            habit.last_sent = now
                            habit.save()
                        except Exception as e:
                            print(
                                f"Не удалось отправить сообщение пользователю {habit.owner.telegram_id}: {e}"
                            )
