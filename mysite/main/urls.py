from django.urls import path
from .views import home

app = "home"
urlpatterns = [
    path("", home, name='main')
]