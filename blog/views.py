from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import BlogPost

# Create your views here.


def all_blog_posts(request):
    """A view to show all blog posts"""

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')
    blog_posts_sidebar = BlogPost.objects.filter(status=1).order_by('-created_on')
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('blog'))
            
            queries = Q(title__icontains=query) | Q(body__icontains=query)
            blog_posts = blog_posts.filter(queries)

    context = {
        'blog_posts': blog_posts,
        'blog_posts_sidebar': blog_posts_sidebar,
        'search_term': query,
    }

    return render(request, 'blog/blog.html', context)


def post_detail(request, blog_id):
    """ A view to show specific blog posts """

    blog_post = get_object_or_404(BlogPost, pk=blog_id)
    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')

    context = {
        "blog_post": blog_post,
        "blog_posts": blog_posts
    }

    return render(request, 'blog/post_detail.html', context)
