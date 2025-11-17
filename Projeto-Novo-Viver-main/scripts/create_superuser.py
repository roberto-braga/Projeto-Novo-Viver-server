from django.contrib.auth import get_user_model


username = "admin"
email = "admin@novoviver.org.br"
password = "Admin123!"

User = get_user_model()
user, created = User.objects.get_or_create(
    username=username,
    defaults={"email": email, "is_staff": True, "is_superuser": True},
)

user.email = email
user.is_staff = True
user.is_superuser = True
user.set_password(password)
user.save()

print(("Created" if created else "Updated"), f"superuser '{username}'")
