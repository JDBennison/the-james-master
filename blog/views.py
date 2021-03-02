from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.


def all_blog_posts(request):
    """A view to show all blog posts"""

    blog_posts = BlogPost.objects.filter(status=1).order_by('-created_on')

    context = {
        "blog_posts": blog_posts
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
