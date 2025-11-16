from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ScheduleEntryForm
from .models import ScheduleEntry

@staff_member_required
def manage(request):
    if request.method == "POST":
        form = ScheduleEntryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Atividade adicionada ao cronograma.")
            return redirect("schedule:manage")
    else:
        form = ScheduleEntryForm()
    entries = ScheduleEntry.objects.order_by("day", "shift", "activity")
    return render(request, "schedule/manage.html", {"form": form, "entries": entries})


@staff_member_required
def delete(request, pk):
    entry = get_object_or_404(ScheduleEntry, pk=pk)
    entry.delete()
    messages.success(request, "Atividade removida.")
    return redirect("schedule:manage")
