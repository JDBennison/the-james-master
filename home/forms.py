from .models import Subscribe
from django import forms


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('subscribe_email',)
