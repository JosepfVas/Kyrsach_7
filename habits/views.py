from rest_framework import generics
from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated

from habits.tasks import send_message_to_tg_bot


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.owner = self.request.user
        send_message_to_tg_bot()
        new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр информации об одной привычке"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListAPIView(generics.ListAPIView):
    """Вывод списка привычек пользователя"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            queryset = Habit.objects.all().filter(owner=user)
        else:
            queryset = Habit.objects.all()
        return queryset


class PublicHabitListAPIView(generics.ListAPIView):
    """Вывод списка публичных привычек"""

    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
