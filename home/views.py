from django.shortcuts import render, reverse, redirect
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from blog.models import BlogPost
from .forms import SubscriptionForm, ContactForm

# Create your views here.


def index(request):
    """ A view to return the index page """

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')[:3]

    if request.method == 'POST':
        if 'subscribe_email' in request.POST:
            subscription_form = SubscriptionForm(request.POST)
            if subscription_form.is_valid():
                subscription_form.save()
                messages.success(request, "You have subscribed to our newsletter!")
            else:
                messages.error(request, "That is not a valid email!")
                return redirect(reverse('home'))
        if 'message' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                subject = contact_form.cleaned_data['subject']
                from_email = contact_form.cleaned_data['from_email']
                message = contact_form.cleaned_data['message']
                try:
                    send_mail(subject, message, from_email, ['jamesbennison88@gmail.com'])
                except BadHeaderError:
                    messages.error(request, "Invalid header found!")
                    return redirect(reverse('home'))
                messages.success(request, "Thank you for your message. We will be in touch very soon!")
    else:
        subscription_form = SubscriptionForm()
        contact_form = ContactForm()

    context = {
        'blog_posts': blog_posts,
        'subscription_form': subscription_form,
        'contact_form': contact_form,
    }

    return render(request, 'home/index.html', context)


def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')
