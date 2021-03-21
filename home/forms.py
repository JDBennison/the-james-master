from .models import Subscribe
from django import forms


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('subscribe_email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # add a "form-control" class to the form input
        # for enabling bootstrap
        for field in self.fields.keys():
            self.fields[field].widget.attrs['class'] = 'form-control border border-black rounded-0'

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
