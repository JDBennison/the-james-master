from django.shortcuts import render
from .models import BlogPost

# Create your views here.


class PostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'post_detail.html'