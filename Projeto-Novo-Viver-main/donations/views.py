from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm


def donate(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Doação registrada! Muito obrigado pela sua contribuição.")
            return redirect("donations:donate")
    else:
        form = DonationForm()
    return render(request, "donations/doacao.html", {"form": form})
