from django.shortcuts import render, redirect, reverse, get_object_or_404
from posts.models import Post
from comments.models import Comment
from comments.forms import CommentForm
from django.http import HttpResponseRedirect


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
            new_comment.name = request.user
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


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        comment.delete()
        return redirect('posts')
    return render(request, "comments/comments_delete.html", {'comment': comment})
