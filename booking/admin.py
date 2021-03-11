from django.contrib import admin
from .models import Booking

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'service', 'user', 'players', 'booked')
    list_filter = ('date', 'booked')
