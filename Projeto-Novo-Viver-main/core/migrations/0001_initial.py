from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Nome")),
                ("email", models.EmailField(max_length=254, verbose_name="E-mail")),
                ("message", models.TextField(verbose_name="Mensagem")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Criado em"),
                ),
            ],
            options={
                "verbose_name": "Contato",
                "verbose_name_plural": "Contatos",
            },
        ),
    ]
