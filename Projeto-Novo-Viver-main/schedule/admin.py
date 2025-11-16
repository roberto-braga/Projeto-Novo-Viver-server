from django.contrib import admin
from .models import ScheduleEntry


@admin.register(ScheduleEntry)
class ScheduleEntryAdmin(admin.ModelAdmin):
    list_display = ("day", "shift", "activity", "created_at")
    list_filter = ("day", "shift")
    search_fields = ("activity",)
