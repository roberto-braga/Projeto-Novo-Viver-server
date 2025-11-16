from django.db import models


class Contact(models.Model):
    name = models.CharField("Nome", max_length=120)
    email = models.EmailField("E-mail")
    phone = models.CharField("Telefone", max_length=30, blank=True)
    message = models.TextField("Mensagem")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)

    def __str__(self):
        return f"Contato de {self.name}"

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"
