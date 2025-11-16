from django.contrib import admin
from .models import Participation


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)
