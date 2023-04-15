from django.urls import path
from . import views

urlpatterns = [
    path("", views.christmas, name="xmas"),
    path("home", views.index, name="index")
]