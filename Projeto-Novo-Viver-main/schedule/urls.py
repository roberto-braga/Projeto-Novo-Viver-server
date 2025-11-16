from django.urls import path
from . import views

app_name = "schedule"

urlpatterns = [
    path("manage/", views.manage, name="manage"),
    path("delete/<int:pk>/", views.delete, name="delete"),
]