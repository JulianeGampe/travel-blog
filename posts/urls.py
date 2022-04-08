from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts, name='posts'),
    path('like/<slug:slug>', views.likes, name='likes'),
    path('delete_post/<post_id>/', views.delete_post, name='delete_post'),
    path('edit_post/<post_id>/', views.edit_post, name='edit_post'),
]
