from .models import Post
from django import forms


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)
        