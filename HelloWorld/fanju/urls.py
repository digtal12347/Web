from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.hello),
    path("fanju/", views.fanju, name="fj"),
    path("second/", views.second),
]
