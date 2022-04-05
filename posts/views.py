from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponseRedirect


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)


def likes(request,slug):
    post = Post.objects.get(slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('comments', args=[slug]))
    