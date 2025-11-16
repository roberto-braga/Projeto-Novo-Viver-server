from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "amount", "kind", "created_at")
    search_fields = ("name", "email", "kind")
    list_filter = ("kind", "created_at")
