from django.shortcuts import render, redirect
from .models import Post
from comments.forms import CommentForm


def posts(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'posts/posts.html', context)


def comments(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.filter(approved=True).order_by("-created")
    new_comment = None

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post 
            new_comment.save()

    else:
        form = CommentForm()
  
    return render(
        request, 'comments/comments.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'form': form}
        )
