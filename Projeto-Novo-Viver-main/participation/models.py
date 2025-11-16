from django.db import models


class Participation(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.name}"

    class Meta:
        verbose_name = "Participação"
        verbose_name_plural = "Participações"
