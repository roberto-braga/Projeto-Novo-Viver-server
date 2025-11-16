from django.db import models


class Donation(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    kind = models.CharField(max_length=50, blank=True, help_text="Tipo de doação (dinheiro, alimentos, etc.)")
    message = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doação de {self.name}"

    class Meta:
        verbose_name = "Doação"
        verbose_name_plural = "Doações"
