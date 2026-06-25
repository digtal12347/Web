from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("live1/", views.live1),
    path("live2/", views.live2),
]
