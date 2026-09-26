from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoModelTests(TestCase):

    def test_todo_creation(self):
        todo = Todo.objects.create(title="Learn CI/CD")

        self.assertEqual(todo.title, "Learn CI/CD")
        self.assertFalse(todo.isCompleted)

    def test_todo_string_representation(self):
        todo = Todo.objects.create(title="Docker")

        self.assertEqual(str(todo), "Docker")


class TodoViewTests(TestCase):

    def setUp(self):
        self.todo = Todo.objects.create(title="Test Todo")

    def test_index_view(self):
        response = self.client.get(reverse("todos:index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_add_todo(self):
        response = self.client.post(
            reverse("todos:add"),
            {"title": "New Todo"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            Todo.objects.filter(title="New Todo").exists()
        )

    def test_update_todo(self):
        response = self.client.post(
            reverse("todos:update", args=[self.todo.id]),
            {"isCompleted": "on"},
        )

        self.assertEqual(response.status_code, 302)

        self.todo.refresh_from_db()

        self.assertTrue(self.todo.isCompleted)

    def test_delete_todo(self):
        todo_id = self.todo.id

        response = self.client.get(
            reverse("todos:delete", args=[todo_id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Todo.objects.filter(id=todo_id).exists())
