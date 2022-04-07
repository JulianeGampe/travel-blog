from posts.models import Post
from comments.models import Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)

