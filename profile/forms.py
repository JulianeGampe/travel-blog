from posts.models import Post
from comments.models import Comment
from django import forms
from cloudinary.forms import CloudinaryFileField

class PostForm(forms.ModelForm):
    image = CloudinaryFileField(
        options= {
            'folder': 'travelblogproject'
        }
    )
    class Meta:
        model = Post
        fields = ('title', 'slug', 'status', 'image', 'content',)

