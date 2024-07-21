from datetime import timedelta

from django.db import models

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    """ Модель привычек """

    PERIODIC_CHOICES = [
        (1, "Ежедневно"),
        (2, "Каждые 2 дня"),
        (3, "Каждые 3 дня"),
        (4, "Каждые 4 дня"),
        (5, "Каждые 5 дней"),
        (6, "Каждые 6 дней"),
        (7, "Еженедельно"),
    ]

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="владелец",
    )
    place = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Место выполнения привычки"
    )
    time = models.TimeField(
        null=True, blank=True, verbose_name="Время выполнения привычки"
    )
    action = models.CharField(max_length=250, verbose_name="Действие")
    positive_habit = models.BooleanField(
        default=True, verbose_name="Положительная привычка"
    )
    linked_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        on_delete=models.CASCADE,
    )
    periodic = models.IntegerField(
        choices=PERIODIC_CHOICES, default=1, verbose_name="Периодичность"
    )
    reward = models.CharField(
        max_length=250, null=True, blank=True, verbose_name="Вознаграждение"
    )
    habit_time = models.DurationField(
        default=timedelta(minutes=2), verbose_name="Время на выполнение привычки"
    )
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")
    last_sent = models.DateTimeField(
        null=True, blank=True, verbose_name="Последняя отправка"
    )

    def __str__(self):
        return f"{self.owner} будет делать {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
