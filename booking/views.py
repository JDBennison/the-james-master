from django.shortcuts import render
from .models import Booking

# Create your views here.


def view_booking(request):
    """ A view that renders the first stage of booking """

    available_dates = Booking.objects.filter(booked=False).order_by('date')

    context = {
        'available_dates': available_dates,
    }

    return render(request, 'booking/booking.html', context)
