from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Booking(models.Model):
    INTRO = 'IN'
    ONE_SHOT = 'OS'
    CAMPAIGN = 'OC'
    SERVICE = [
        (INTRO, 'Introduction To DnD'),
        (ONE_SHOT, 'One Shot Adventure'),
        (CAMPAIGN, 'Ongoing Campaign')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    time = models.TimeField(auto_now=False, null=True, blank=True)
    date = models.DateField(auto_now=False, null=True, blank=True)
    service = models.CharField(max_length=2, choices=SERVICE, null=True, blank=True)
    players = models.IntegerField(null=True, blank=True)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return 'Booking {} at {}'.format(self.date, self.time)
