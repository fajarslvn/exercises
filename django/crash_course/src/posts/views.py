from django.shortcuts import render
from .models import Post # Set 5

def post_list(request): # Set 3
    posts = Post.objects.all() # Set 5
    context = {
        'post_list': posts
    } # Set 5
    return render(request, 'posts/post_list.html', context) # Set 4
