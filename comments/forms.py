from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    '''
    CommentForm to create a new comment
    '''
    class Meta:
        model = Comment
        fields = ('body',)
