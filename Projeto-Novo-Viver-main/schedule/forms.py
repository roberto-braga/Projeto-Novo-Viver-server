from django import forms
from .models import ScheduleEntry


class ScheduleEntryForm(forms.ModelForm):
    class Meta:
        model = ScheduleEntry
        fields = ["day", "shift", "activity"]