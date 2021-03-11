from django.contrib import admin
from .models import Subscribe

# Register your models here.

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('subscribe_email', 'subscribed')
