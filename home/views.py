from django.shortcuts import render
from django.contrib import messages
from blog.models import BlogPost
from .forms import SubscriptionForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]

    if request.method == 'POST':
        subscription = SubscriptionForm(request.POST)
        if subscription.is_valid:
            subscription.save()
            messages.success(request, "You have subscribed to our newsletter!")

    context = {
        "blog_posts": blog_posts
    }

    return render(request, 'home/index.html', context)


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')
