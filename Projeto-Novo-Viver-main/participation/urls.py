from django.urls import path
from . import views

app_name = "participation"

urlpatterns = [
    path("", views.apply, name="apply"),
]