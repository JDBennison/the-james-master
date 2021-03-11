from django.shortcuts import render, reverse
from django.contrib import messages
from blog.models import BlogPost
from .forms import SubscriptionForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]

    if request.method == 'POST':
        subscription_form = SubscriptionForm(request.POST)
        if subscription_form.is_valid():
            subscription_form.save()
            messages.success(request, "You have subscribed to our newsletter!")
        else:
            reverse('home')
            messages.error(request, "That is not a valid email!")
    else:
        subscription_form = SubscriptionForm()

    context = {
        'blog_posts': blog_posts,
        'form': subscription_form,
    }

    return render(request, 'home/index.html', context)


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')
