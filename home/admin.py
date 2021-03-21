from django.contrib import admin
from .models import Subscribe


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('subscribe_email', 'subscribed')
