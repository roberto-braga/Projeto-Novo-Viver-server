from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("contato/", views.contato, name="contato"),          
    path("contato/enviar/", views.submit_contact, name="contact"),
]
