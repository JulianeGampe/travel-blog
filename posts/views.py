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

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post 
            comment.save()

            return redirect('comments', slug=post.slug)
    else:
        form = CommentForm()
  
    return render(
        request, 'comments/comments.html', {'post': post, 'form': form}
        )
