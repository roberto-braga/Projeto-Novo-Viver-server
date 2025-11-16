from django.db import models


class ScheduleEntry(models.Model):
    DAY_CHOICES = [
        ("seg", "Seg"),
        ("ter", "Ter"),
        ("qua", "Qua"),
        ("qui", "Qui"),
        ("sex", "Sex"),
    ]
    SHIFT_CHOICES = [
        ("manha", "Manhã"),
        ("tarde", "Tarde"),
        ("noite", "Noite"),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    shift = models.CharField(max_length=6, choices=SHIFT_CHOICES)
    activity = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["day", "shift", "activity"]
        verbose_name = "Atividade do Cronograma"
        verbose_name_plural = "Atividades do Cronograma"

    def __str__(self):
        return f"{self.get_day_display()} {self.get_shift_display()} - {self.activity}"
