from django.db import models


class Comment(models.Model):
    '''
    Model for the comments of the posts
    '''
    post = models.ForeignKey(
        'posts.Post', on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        Sorts comments by date created
        '''
        ordering = ["-created"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
