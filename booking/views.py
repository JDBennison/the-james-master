from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse

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


def checkout(request):
    """
    A view to see your final order and purchase it
    """

    return render(request, 'booking/checkout.html')


def save_booking(request):
    players = int(request.POST.get('players', None))
    service = request.POST.get('service', None)
    date = request.POST.get('date', None)
    checkout = request.session.get('checkout', {})
    checkout[date] = players

    request.session['checkout'] = checkout
    print(request.session['checkout'])
    return redirect('checkout')
