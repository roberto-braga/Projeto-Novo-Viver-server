from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib import messages
from schedule.models import ScheduleEntry
from .forms import ContactForm


def home(request):
    schedule_map = {d: {s: [] for s in ["manha", "tarde", "noite"]} for d in ["seg", "ter", "qua", "qui", "sex"]}
    for entry in ScheduleEntry.objects.all():
        schedule_map[entry.day][entry.shift].append(entry.activity)
    return render(request, "index.html", {"schedule_map": schedule_map})


class AdminAwareLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        redirect_url = self.get_redirect_url()
        if redirect_url:
            return redirect_url
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return reverse("admin:index")
        return reverse("core:home")


def contato(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada! Obrigado pelo contato.")
            form = ContactForm()
        else:
            messages.error(request, "Verifique os campos e tente novamente.")

    else:
        form = ContactForm()


    return render(request, "contato.html", {"form": form})

