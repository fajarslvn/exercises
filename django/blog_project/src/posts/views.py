from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

def post_list(request):
    post = Post.objects.all()
    context = {
        'post_list': post,
    }
    return render(request,'post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'post_detail.html', context)

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        'form': form,
        'form_type': 'Create',
    }
    return render(request, 'post_create.html', context)

def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts')
    context = {
        'form': form,
        'form_type': 'Update',
    }
    return render(request, 'post_create.html', context)

def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/posts')