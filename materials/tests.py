from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from materials.models import Course, Lesson, Subscription
from django.urls import reverse

class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(title="Test Course", description="Test Course", owner=self.user)
        self.lesson = Lesson.objects.create(title="Test Lesson", description="Test Lesson",
                                            course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_create(self):
        url = reverse('materials:lesson_create')
        data = {
            "title": "Test Lesson 2",
            "description": "Test Lesson 2",
            "course": self.course.pk,
            "url": "https://www.youtube.com/test2/')"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson_update', args=(self.lesson.pk,))
        data = {
            "title": "Test Lesson 2/1"
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Test Lesson 2/1")

    def test_lesson_retriew(self):
        url = reverse('materials:lesson_retriew', args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_lesson_delete(self):
        url = reverse('materials:lesson_delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_lesson_list(self):
        url = reverse('materials:lesson_list')
        response = self.client.get(url)
        data = response.json()
        result = {'count': 1,
                  'next': None,
                  'previous': None,
                  'results': [
                      {'id': self.lesson.pk,
                       'url': None,
                       'title': self.lesson.title,
                       'description': self.lesson.description,
                       'image': None,
                       'course': self.lesson.course.pk,
                       'owner': self.lesson.owner.pk}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru")
        self.course = Course.objects.create(title="Test Course", description="Test Course", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription(self):
        url = reverse('materials:subscription_create')
        data = {
            "course": self.course.pk
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 1)
        self.assertEqual(response.json(), {"messages": "подписка оформлена"})

    def test_subscription_delete(self):
        url = reverse('materials:subscription_create')
        data = {
            "course": self.course.pk
        }
        self.client.post(url, data)
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Subscription.objects.all().count(), 0)
        self.assertEqual(response.json(), {"messages": "подписка удалена"})
