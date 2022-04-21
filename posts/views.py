from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponseRedirect
from .forms import PostEditForm
from datetime import datetime
from django.contrib import messages


def posts(request):
    posts = Post.objects.all()
    template = 'posts/posts.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def likes(request, slug):
    post = Post.objects.get(slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('comments', args=[slug]))


def edit_post(request, post_id):
    edited_post = get_object_or_404(Post, id=post_id)
    template = "posts/posts_edit.html"

    if request.method == 'POST':
        edit_form = PostEditForm(request.POST, instance=edited_post)
        if edit_form.is_valid():
            edited_post.updated = datetime.now()
            edited_post = edit_form.save(commit=False)
            edited_post.save()
            messages.success(request, 'You have edited the post.')
            return redirect('posts')
    edit_form = PostEditForm(instance=edited_post)

    context = {
        'edit_form': edit_form,
        'edited_post': edited_post
    }
    return render(request, template, context)


def delete_post(request, post_id):
    posts_delete = get_object_or_404(Post, id=post_id)
    template = "posts/posts_delete.html"
    context = {
        'posts_delete': posts_delete
    }

    if request.method == "POST":
        posts_delete.delete()
        messages.success(request, 'You have deleted the post.')
        return redirect('posts')
    return render(request, template, context)
