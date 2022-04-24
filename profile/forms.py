from posts.models import Post
from django import forms
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    '''
    PostForm to create a post from the frontend
    '''
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)
