from django.db import models
from datetime import datetime


# zawsze gdy dodajemy model to w cmd 'python manage.py makemigrations contacts' . musi być wcześniej dodane w settings.py w INSTALLED_APPS
class Contact(models.Model):
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    # zarejestrowany user robiący zapytanie, nie musi być zalogowany (ale może i możemy wtedy widzieć o nim)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


