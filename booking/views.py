from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Booking, Order
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
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        if 'stripe-submit' in request.POST:
            full_name = request.POST['full_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            comment = request.POST['comment']
            players = int(request.POST['players'])
            service = request.POST['service']
            date_id = request.POST['date_id']
            location = request.POST['location']
            form_data = {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'players': players,
                'service': service,
                'date_id': date_id,
                'location': location,
                'comment': comment,
            }
            order_form = OrderForm(form_data)
            if order_form.is_valid():
                order = order_form.save()
                booking_date = get_object_or_404(Booking, pk=date_id)
                if booking_date.booked is False:
                    new_booking = Booking(
                        service=request.POST['service'],
                        players=int(request.POST['players']),
                        booked=True,
                    )
                    new_booking.save()
                elif booking_date.booked is True:
                    messages.error(request, (
                        "I'm afraid that date has been booked. Please try a different date.")
                    )
                    order.delete()
                    return redirect(reverse('booking'))
                request.session['save_info'] = 'save_info' in request.POST
                return redirect(reverse('checkout_success', args=[order.order_number]))
            else:
                messages.error(request, 'There was an error with your form. Please double check your information.')
        elif 'booking-submit' in request.POST:
            full_name = request.POST['full_name']
            email = request.POST['email']
            phone_number = request.POST['phone_number']
            comment = request.POST['comment']
            players = int(request.POST['players'])
            service = request.POST['service']
            date_id = request.POST['date']
            date = get_object_or_404(Booking, pk=date_id)
            location = request.POST['location']
            if service == 'IN':
                cost = players * settings.INTRO_COST
            elif service == 'OS':
                cost = players * settings.ONE_SHOT_COST
            elif service == 'OC':
                cost = players * settings.CAMPAIGN_COST
            else:
                cost = 0

            stripe_total = round(cost * 100)
            stripe.api_key = stripe_secret_key
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            context = {
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
                'players': players,
                'service': service,
                'location': location,
                'date': date,
                'cost': cost,
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'comment': comment,
                'date_id': date_id
            }

            if not stripe_public_key:
                messages.warning(request, 'Stripe public key is missing. \
                    Did you forget to set it in your environment?')

            return render(request, 'booking/checkout.html', context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    template = 'booking/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
