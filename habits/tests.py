from datetime import timedelta

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from users.models import User
from habits.models import Habit


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@example.com", password="test")
        self.habit = Habit.objects.create(
            owner=self.user,
            place="Дома",
            time="06:00:00",
            action="Утренняя разминка сразу после будильника",
            positive_habit=True,
            periodic=7,
            reward="Выпить стакан сока",
            habit_time=timedelta(seconds=120),
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habit_create")
        data = {
            "owner": self.user.id,
            "place": "test",
            "time": "06:00:00",
            "action": "test",
            "positive_habit": True,
            "periodic": 2,
            "reward": "test",
            "habit_time": "00:01:30",
            "is_public": False,
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_list(self):
        url = reverse("habits:habit_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve(self):
        url = reverse("habits:habit_retrieve", kwargs={"pk": self.habit.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        url = reverse("habits:habit_update", kwargs={"pk": self.habit.id})
        data = {"place": "На улице"}
        response = self.client.patch(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "На улице")

    def test_habit_delete(self):
        url = reverse("habits:habit_delete", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_time(self):
        url = reverse("habits:habit_create")
        data = {
            "owner": self.user.id,
            "place": "test",
            "time": "06:00:00",
            "action": "test",
            "positive_habit": True,
            "periodic": 2,
            "reward": "test",
            "habit_time": "00:03:30",
            "is_public": False,
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_periodic_8(self):
        url = reverse("habits:habit_create")
        data = {
            "owner": self.user.id,
            "place": "test",
            "time": "06:00:00",
            "action": "test",
            "positive_habit": True,
            "periodic": 8,
            "reward": "test",
            "habit_time": "00:01:30",
            "is_public": False,
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_periodic_zero(self):
        url = reverse("habits:habit_create")
        data = {
            "owner": self.user.id,
            "place": "test",
            "time": "06:00:00",
            "action": "test",
            "positive_habit": True,
            "periodic": 0,
            "reward": "test",
            "habit_time": "00:01:30",
            "is_public": False,
        }

        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
