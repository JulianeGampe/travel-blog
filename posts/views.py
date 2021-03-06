from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponseRedirect
from .forms import PostEditForm
from datetime import datetime
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required


def posts(request):
    posts = Post.objects.all()
    template = 'posts/posts.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)


def likes(request, slug):
    '''
    View to like/unlike the post
    '''
    post = Post.objects.get(slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('comments', args=[slug]))


@login_required
def edit_post(request, post_id):
    '''
    View to edit post from the frontend
    '''
    edited_post = get_object_or_404(Post, id=post_id)
    template = "posts/posts_edit.html"

    if request.user.username != 'mia_travels' and \
            not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('posts')
    if request.method == 'POST':
        edit_form = PostEditForm(
            request.POST,
            request.FILES,
            instance=edited_post
            )
        if edit_form.is_valid():
            edited_post.updated = datetime.now()
            edited_post = edit_form.save(commit=False)
            edited_post.save()
            messages.success(request, 'You have edited the post.')
            return redirect('posts')
    edit_form = PostEditForm(instance=edited_post)

    context = {
        'edit_form': edit_form,
        'edited_post': edited_post,
        'TINYMCE_API': settings.TINYMCE_API,
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    '''
    View to delete post from the frontend
    '''
    posts_delete = get_object_or_404(Post, id=post_id)
    template = "posts/posts_delete.html"
    context = {
        'posts_delete': posts_delete
    }

    if request.user.username != 'mia_travels' and \
            not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('posts')
    if request.method == "POST":
        posts_delete.delete()
        messages.success(request, 'You have deleted the post.')
        return redirect('posts')
    return render(request, template, context)
