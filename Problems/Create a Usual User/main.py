from django.contrib.auth.models import User


User.objects.create_user(username="FirstUser", password="HyPerPasS", email="firstuser@example.com")
