from django.shortcuts import render
from .models import Booking
from .forms import OrderForm

# Create your views here.


def view_booking(request):
    """ A view that renders the first stage of booking """

    available_dates = Booking.objects.filter(booked=False).order_by('date')
    order_form = OrderForm()

    context = {
        'available_dates': available_dates,
        'order_form': order_form,
    }

    return render(request, 'booking/booking.html', context)
