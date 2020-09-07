from django.urls import path
from rest_framework import routers
from todo_app import views

router = routers.SimpleRouter()
router.register(r'todo', views.TodoViewSet)

urlpatterns = router.urls
