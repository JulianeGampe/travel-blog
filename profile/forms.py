from posts.models import Post
from comments.models import Comment
from django import forms
from cloudinary.forms import CloudinaryFileField
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):

    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 30}))

    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)
