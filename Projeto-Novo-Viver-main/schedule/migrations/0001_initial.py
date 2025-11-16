from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ScheduleEntry",
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
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("seg", "Seg"),
                            ("ter", "Ter"),
                            ("qua", "Qua"),
                            ("qui", "Qui"),
                            ("sex", "Sex"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "shift",
                    models.CharField(
                        choices=[
                            ("manha", "Manhã"),
                            ("tarde", "Tarde"),
                            ("noite", "Noite"),
                        ],
                        max_length=6,
                    ),
                ),
                ("activity", models.CharField(max_length=200)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["day", "shift", "activity"],
            },
        ),
    ]
