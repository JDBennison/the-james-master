from django.contrib import admin
from .models import Booking, Order

# Register your models here.


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'service', 'user_profile', 'players', 'booked')
    list_filter = ('date', 'booked')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'booked_on', 'cost',)
    fields = ('order_number', 'user_profile', 'date_booked', 'players'
              'service', 'full_name', 'email', 'phone_number',
              'comment', 'location', 'booked_on', 'cost',)
    list_display = ('order_number', 'date_booked', 'players',
                    'service', 'full_name', 'comment',  'location',)
    ordering = ('-booked_on',)
