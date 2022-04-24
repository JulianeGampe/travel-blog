from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from comments.models import Comment
from profile.forms import PostForm
from django.contrib import messages


def profile(request):
    '''
    View to create a new post from the frontend
    '''
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.author = request.user
            post_form.profile = profile
            post_form.save()
            messages.success(request, 'Your post was created.')

            return redirect('posts')

    else:
        post_form = PostForm()

    comments = Comment.objects.all()

    template = 'profile/profile.html'
    context = {
        'post_form': post_form,
        'comments': comments,
    }
    return render(request, template, context)


def approve(request, comment_id):
    '''
    View to approve a comment from the frontend
    '''
    comment = get_object_or_404(Comment, id=comment_id)
    template = "profile/approve.html"
    context = {
        'comment': comment
    }

    if request.method == "POST":
        comment.approved = True
        comment.save()
        messages.success(request, 'You approved the comment.')
        return redirect('profile')
    return render(request, template, context)
