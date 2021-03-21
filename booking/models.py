import uuid

from django.db import models

from profiles.models import UserProfile


class Booking(models.Model):
    INTRO = 'IN'
    ONE_SHOT = 'OS'
    CAMPAIGN = 'OC'
    SERVICE = [
        (INTRO, 'Introduction To DnD'),
        (ONE_SHOT, 'One Shot Adventure'),
        (CAMPAIGN, 'Ongoing Campaign')
    ]
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    time = models.TimeField(auto_now=False, null=True, blank=True)
    date = models.DateField(auto_now=False, null=True, blank=True)
    service = models.CharField(max_length=2, choices=SERVICE, null=True, blank=True)
    players = models.IntegerField(null=True, blank=True)
    booked = models.BooleanField(default=False)

    def __str__(self):
        return '{} at {}'.format(self.date, self.time)


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
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date_booked = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=False)
    booked_on = models.DateTimeField(auto_now_add=True)
    players = models.IntegerField(null=True, blank=False)
    service = models.CharField(max_length=2, choices=SERVICE, null=True, blank=False)
    location = models.CharField(max_length=3, choices=LOCATION, null=True, blank=False, default='ONL')
    comment = models.TextField(null=False, blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)

    def __str__(self):
        return self.order_number

    def _generate_order_number(self):
        """
        Generate a random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already and update the cost
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)
