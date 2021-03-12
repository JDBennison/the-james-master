from home.forms import SubscriptionForm
from django.conf import settings


def subscription_form(request):
    form = SubscriptionForm()
    context = {
        'subscription_form': form,
        'intro_cost': settings.INTRO_COST,
        'one_shot_cost': settings.ONE_SHOT_COST,
        'campaign_cost': settings.CAMPAIGN_COST,

    }
    return context
