from django.contrib import admin
from .models import Post


# Register the Post model on the admin site.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created')
