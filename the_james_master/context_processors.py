from home.forms import SubscriptionForm


def subscription_form(request):
    form = SubscriptionForm()
    context = {'subscription_form': form}
    return context
