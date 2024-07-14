from rest_framework import generics
from habits.models import Habit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""

    serializer_class = HabitSerializer

    # def perform_create(self, serializer):
    #     new_habit = serializer.save()
    #     new_habit.owner = self.request.user
    #     create_schedule(new_habit)
    #     new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр информации об одной привычке"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    queryset = Habit.objects.all()


class HabitListAPIView(generics.ListAPIView):
    """Вывод списка привычек пользователя"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_queryset(self):
        queryset = Habit.objects.filter(owner=self.request.user)
        return queryset
