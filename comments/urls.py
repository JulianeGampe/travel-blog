from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.comments, name='comments'),
    path('edit/<comment_id>/', views.edit_comment, name='edit'),
    path('delete/<comment_id>/', views.delete_comment, name='delete'),
]
