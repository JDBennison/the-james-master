from django.shortcuts import render


def profile(request):
    """ Dispaly user Profile. """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
