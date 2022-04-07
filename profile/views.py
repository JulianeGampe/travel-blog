from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from comments.models import Comment
from profile.forms import PostForm

def profile(request):

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        

        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.author = request.user
            post_form.profile = profile
            post_form.save()

            return redirect('/')

    else:
        post_form = PostForm()

    comments = Comment.objects.all()
  
    return render(
        request, 
        'profile/profile.html', 
        {
            'post_form': post_form,
            'comments': comments,
        }
    )


def approve(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":
        comment.approved = True
        comment.save()
        return redirect('profile')
    return render(request, "profile/approve.html", {'comment': comment})
