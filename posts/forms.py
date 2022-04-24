from .models import Post
from django import forms
from tinymce.widgets import TinyMCE


class PostEditForm(forms.ModelForm):
    '''
    PostEditForm to edit the post on the frontend
    '''
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)
