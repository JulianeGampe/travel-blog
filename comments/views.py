from django.shortcuts import render, redirect, reverse, get_object_or_404
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def comments(request, slug):
    '''
    View to create a new comment
    '''
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created")
    new_comment = None
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
            messages.info(request, 'Your comment is awaiting approval.')

    else:
        form = CommentForm()

    template = 'comments/comments.html'
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'form': form,
        'liked': liked
    }
    return render(request, template, context)


def edit_comment(request, comment_id):
    '''
    View to edit an existing comment
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    edited_comment = None
    if request.method == 'POST':
        edit_form = CommentForm(request.POST, instance=comment)
        if edit_form.is_valid():
            edited_comment = edit_form.save(commit=False)
            edited_comment.approved = False
            edited_comment.save()
            messages.info(
                request,
                'You have edited your comment. It is awaiting approval.'
                )
    edit_form = CommentForm(instance=comment)
    template = "comments/comments_edit.html"
    context = {
        'edit_form': edit_form,
        'edited_comment': edited_comment
    }
    return render(request, template, context)


def delete_comment(request, comment_id):
    '''
    View to delete a comment
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    template = "comments/comments_delete.html"
    context = {
        'comment': comment
    }

    if request.method == "POST":
        comment.delete()
        messages.success(request, 'You have deleted the comment.')
        return redirect('posts')
    return render(request, template, context)
