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
