from django import forms
from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["name", "email", "phone", "amount", "kind", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 4}),
        }