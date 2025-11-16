from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from core.views import AdminAwareLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("cronograma/", include("schedule.urls")),
    path("doacoes/", include("donations.urls")),
    path("participar/", include("participation.urls")),
    path("login/", AdminAwareLoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
