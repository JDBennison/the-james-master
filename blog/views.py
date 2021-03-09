from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import BlogPost
from .forms import CommentForm

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
    blog_posts_sidebar = BlogPost.objects.filter(status=1).order_by('-created_on')
    comments = blog_post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog_post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'blog_post': blog_post,
        'blog_posts_sidebar': blog_posts_sidebar,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/post_detail.html', context)
