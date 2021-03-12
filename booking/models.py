import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
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

class Order(models.Model):
    INTRO = 'IN'
    ONE_SHOT = 'OS'
    CAMPAIGN = 'OC'
    IN_REAL_LIFE = 'IRL'
    ONLINE = 'ONL'
    SERVICE = [
        (INTRO, 'Introduction To DnD'),
        (ONE_SHOT, 'One Shot Adventure'),
        (CAMPAIGN, 'Ongoing Campaign')
    ]
    LOCATION = [
        (IN_REAL_LIFE, 'In Real Life'),
        (ONLINE, 'Online'),
    ]
    
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_booked = models.DateField(auto_now=False, null=True, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    players = models.IntegerField(null=True, blank=False)
    service = models.CharField(max_length=2, choices=SERVICE, null=True, blank=True)
    location = models.CharField(max_length=3, choices=LOCATION, null=True, blank=False, default='ONL')
    comment = models.EmailField(max_length=254, null=False, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """ 
        Generate a randome unique order number using UUID 
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already and update the cost
        """
        if self.service == 'IN':
            self.cost = self.players * settings.INTRO_COST
        elif self.service == 'OS':
            self.cost = self.players * settings.ONE_SHOT_COST
        elif self.service == 'OC':
            self.cost = self.players * settings.CAMPAIGN_COST
        else:
            self.cost = 0

        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
