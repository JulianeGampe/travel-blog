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


def comments(request, slug):
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
            new_comment.post = post 
            new_comment.save()

    else:
        form = CommentForm()
  
    return render(
        request, 
        'comments/comments.html', 
        {
            'post': post, 
            'comments': comments, 
            'new_comment': new_comment, 
            'form': form,
            'liked': liked
        }
    )


def likes(request,slug):
    post = Post.objects.get(slug=slug)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)

    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('comments', args=[slug]))


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('posts')
