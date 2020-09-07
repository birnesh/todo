from django.test import TestCase
from todo_app import models

class TodoTestClass(TestCase):
    """
    tesiting Todo model
    """
    @classmethod
    def setUpTestData(cls):
        models.Todo.objects.create(task='testing is_done for False value',is_done=False)
        models.Todo.objects.create(task='testing is_done for True value',is_done=True)

    def test_task_field_max_length(self):
        todo = models.Todo.objects.first()
        max_length = todo._meta.get_field('task').max_length
        self.assertEquals(max_length, 100)

    def test_is_done_field(self):
        todo_1 = models.Todo.objects.first()
        todo_2 = models.Todo.objects.get(no=2)
        self.assertTrue(todo_1.is_done == False)
        self.assertTrue(todo_2.is_done == True)

    