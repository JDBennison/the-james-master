from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Booking
from .forms import OrderForm

import stripe

# Create your views here.


def booking(request):
    """ A view that renders the first stage of booking """
    available_dates = Booking.objects.filter(booked=False).order_by('date')
    order_form = OrderForm()

    context = {
        'available_dates': available_dates,
        'order_form': order_form,
    }

    return render(request, 'booking/booking.html', context)


def checkout(request):
    """
    A view to see your final order and purchase it
    """
    players = int(request.POST.get('players', None))
    service = request.POST.get('service', None)
    date_id = request.POST.get('date', None)
    date = get_object_or_404(Booking, pk=date_id)
    location = request.POST.get('location', None)
    if service == 'IN':
        cost = players * settings.INTRO_COST
    elif service == 'OS':
        cost = players * settings.ONE_SHOT_COST
    elif service == 'OC':
        cost = players * settings.CAMPAIGN_COST
    else:
        cost = 0
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    checkout = request.session.get('checkout', {})
    if not checkout:
        messages.error(request, "You have not selected a session")
        return redirect(reverse('booking'))

    stripe_total = round(cost * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'players': players,
        'service': service,
        'location': location,
        'date': date,
        'cost': cost,
    }

    return render(request, 'booking/checkout.html', context)
