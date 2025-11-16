from django import forms
from .models import Participation


class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }