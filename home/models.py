from django.db import models

# Create your models here.


class Subscribe(models.Model):
    subscribe_email = models.EmailField(max_length=254, unique=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.subscribe_email
