from django.conf import settings
from django.shortcuts import get_object_or_404
from booking.models import Booking


def booking_details(request):
    booking_date = []
    booking_service = ''
    booking_players = 0
    booking_cost = 0
    booking_location = ''
    booking = request.session.get('checkout', {})

    for date_id, info in booking.items():
        booking = get_object_or_404(Booking, pk=date_id)
        booking_service = info['service']
        booking_players = info['players']
        booking_location = info['location']
        if booking_service == 'IN':
            booking_cost = booking_players * settings.INTRO_COST
        elif booking_service == 'OS':
            booking_cost = booking_players * settings.ONE_SHOT_COST
        elif booking_service == 'OC':
            booking_cost = booking_players * settings.CAMPAIGN_COST
        else:
            booking_cost = 0
        booking_date.append({
            'booking': booking,
            'booking_service': booking_service,
            'booking_players': booking_players,
            'booking_cost': booking_cost,
            'booking_location': booking_location,
        })

    context = {
        'booking_date': booking_date,
        'service': booking_service,
        'players': booking_players,
        'cost': booking_cost,
    }

    return context
