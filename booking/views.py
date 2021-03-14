from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

from .models import Booking
from .forms import OrderForm

import stripe

# Create your views here.


def booking(request):
    """ A view that renders the first stage of booking """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    available_dates = Booking.objects.filter(booked=False).order_by('date')
    order_form = OrderForm()

    # players = request.POST.get('players', None)
    # service = request.POST.get('service', None)
    players = 7
    service = 'IN'
    if service == 'IN':
        cost = players * settings.INTRO_COST
    elif service == 'OS':
        cost = players * settings.ONE_SHOT_COST
    elif service == 'OC':
        cost = players * settings.CAMPAIGN_COST
    else:
        cost = 0

    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=cost,
        currency=settings.STRIPE_CURRENCY,
    )
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \ Did you forget to set it up in your environment?')

    context = {
        'available_dates': available_dates,
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }

    return render(request, 'booking/booking.html', context)


def calculate_cost(request):
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
