from django.conf import settings


def booking_details(request):
    service = ""
    players = 0
    cost = 0

    if service == 'IN':
        cost = players * settings.INTRO_COST
    elif service == 'OS':
        cost = players * settings.ONE_SHOT_COST
    elif service == 'OC':
        cost = players * settings.CAMPAIGN_COST
    else:
        cost = 0
    
    context = {
        'service': service,
        'players': players,
        'cost': cost,
    }

    return context
