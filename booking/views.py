from django.shortcuts import render

# Create your views here.

def view_booking(request):
    """ A view that renders the first stage of booking """

    return render(request, 'booking/booking.html')