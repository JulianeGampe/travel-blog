from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image = CloudinaryField('image', default='placeholder')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
    )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
