from django.contrib.auth.models import User


User.objects.create_superuser(
     username='AdminUser', email='adminuser@example.com', password='UnHacKabLE'
)
