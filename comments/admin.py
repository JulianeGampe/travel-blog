from django.contrib import admin
from .models import Comment


# Register the comments model on the admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created', 'approved')
    list_filter = ('approved', 'created')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
