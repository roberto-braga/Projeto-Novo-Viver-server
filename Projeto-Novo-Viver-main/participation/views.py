from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParticipationForm


def apply(request):
    if request.method == "POST":
        form = ParticipationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada! Entraremos em contato em breve.")
            return redirect("participation:apply")
    else:
        form = ParticipationForm()
    return render(request, "participation/participar.html", {"form": form})
