from django.shortcuts import render
from .models import Booking
from .forms import OrderForm

# Create your views here.


def booking(request):
    """ A view that renders the first stage of booking """

    available_dates = Booking.objects.filter(booked=False).order_by('date')
    order_form = OrderForm()

    context = {
        'available_dates': available_dates,
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HtfbeEEmxKYa1SXAt2nbwmwEljVyfLSFMsh5imlPgdjelJVz36ywLdqa5J0PJXzF10RAHii49hlHtdqqgexsxsN00iGRaEe64',
        'client_secret': 'test client secret'
    }

    return render(request, 'booking/booking.html', context)
