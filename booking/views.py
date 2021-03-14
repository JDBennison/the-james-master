from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
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


def calculate_cost(request):
    print(request.POST.get('csrfmiddlewaretoken'))
    players = int(request.POST.get('players', None))
    service = request.POST.get('service', None)
    if service == 'IN':
        cost = players * settings.INTRO_COST
    elif service == 'OS':
        cost = players * settings.ONE_SHOT_COST
    elif service == 'OC':
        cost = players * settings.CAMPAIGN_COST
    else:
        cost = 0

    return HttpResponse(cost)
